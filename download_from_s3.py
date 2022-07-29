from backup_management import BackupManagement
import zipfile
from data import *


if __name__ == '__main__':
    backup_management = BackupManagement()
    backup_management.download_from_s3()
    with zipfile.ZipFile(DOWNLOAD_S3_FILENAME, 'r') as zip_ref:
        zip_ref.extractall(f"./{DOWNLOAD_S3_FILENAME.replace('.zip', '')}")
