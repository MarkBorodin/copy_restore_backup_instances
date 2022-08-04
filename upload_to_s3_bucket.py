from backup_management import BackupManagement
from data import *


if __name__ == '__main__':
    backup_management = BackupManagement()
    backup_management.upload_to_s3()
