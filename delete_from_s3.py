from backup_management import BackupManagement
from data import *


if __name__ == '__main__':
    backup_management = BackupManagement()
    backup_management.delete_from_s3()
