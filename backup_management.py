from datetime import timedelta

import boto3

from data import *


class BackupManagement(object):
    """
    BackupManagement class
    """

    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
        self.s3 = self.session.resource('s3')
        self.bucket = self.s3.Bucket(S3_BUCKET)

    def show_structure(self):
        """
        show bucket structure
        :return: None
        """
        object_summary_iterator = self.bucket.objects.all()
        for b_object in object_summary_iterator:
            time_delta = datetime.now(b_object.last_modified.tzinfo) - timedelta(days=30)
            print(
                f'{b_object}:' + str(b_object.last_modified) +
                (':old' if time_delta > b_object.last_modified < time_delta else ':new')
            )

    def show_instance_only(self):
        object_summary_iterator = self.bucket.objects.all()
        for b_object in object_summary_iterator:
            if b_object.key.split(sep='/')[0] == INSTANCE_NAME:
                time_delta = datetime.now(b_object.last_modified.tzinfo) - timedelta(days=30)
                print(
                    f'{b_object}:' + str(b_object.last_modified) +
                    (':old' if time_delta > b_object.last_modified < time_delta else ':new')
                )

    def upload_to_s3(
            self,
            filename=UPLOAD_S3_FILENAME,
            key=f'{INSTANCE_NAME}/{UPLOAD_S3_KEY}'
    ):
        """
        upload object to s3 bucket
        :param filename: str
        :param key: str
        :return: None
        """
        with open(filename, 'rb') as data:
            self.bucket.upload_fileobj(Key=key, Fileobj=data)

    def download_from_s3(
            self,
            filename=DOWNLOAD_S3_FILENAME,
            bucket=S3_BUCKET,
            key=f'{INSTANCE_NAME}/{DOWNLOAD_S3_FILENAME}'
    ):
        """
        download object from s3 bucket
        :param filename: str
        :param bucket: str
        :param key: str
        :return: None
        """
        self.s3.meta.client.download_file(Filename=filename, Bucket=bucket, Key=key)

    def delete_from_s3(
            self,
            bucket=S3_BUCKET,
            key=f'{INSTANCE_NAME}/{UPLOAD_S3_KEY}'
    ):
        """
        delete object from s3
        :param bucket: str
        :param key: str
        :return: None
        """
        self.s3.meta.client.delete_object(Bucket=bucket, Key=key)

    @staticmethod
    def is_old_object(b_object):
        """
        Check if object older than 30 days
        :param b_object: class S3.Object(bucket_name, key)
        :return: bool
        """
        time_delta = datetime.now(b_object.last_modified.tzinfo) - timedelta(days=30)
        return True if time_delta > b_object.last_modified < time_delta else False

    def remove_old_copies(self):
        """
        remove old copies from s3
        :return: None
        """
        object_summary_iterator = self.bucket.objects.all()
        for b_object in object_summary_iterator:
            if b_object.key.split(sep='/')[0] == INSTANCE_NAME:
                if self.is_old_object(b_object):
                    self.delete_from_s3(key=b_object.key)
