import os
import time

from data import *


# PATH
base_dir = './'
backup_folder = DOWNLOAD_S3_FILENAME.replace('.zip', '')
snapshot_dir = base_dir + backup_folder + '/'
path_to_local_file: str = snapshot_dir + 'app/config/local.php'


# COMMANDS
chown = f'docker exec {MAUTIC_CONTAINER_NAME} bash -c "chown -R www-data:www-data /var/www/html"'
copy_all = f'docker cp ./{backup_folder}/. {MAUTIC_CONTAINER_NAME}:/var/www/html/.'
restore_dump = f'docker exec -i {DB_CONTAINER_NAME} mysql -u {MYSQL_USER} -p{MYSQL_PASSWORD} {MYSQL_DATABASE} < ./{backup_folder}/dump.sql'


def change_local_file(path_to_local_file):
    with open(path_to_local_file, 'r') as f:
        text = f.read()
        text = text.replace(f"'site_url' => '{OLD_URL}',", f"'site_url' => '{NEW_URL}',")
    with open(path_to_local_file, 'w') as f:
        f.write(text)


if __name__ == '__main__':

    change_local_file(path_to_local_file)
    commands_list = [copy_all, chown, restore_dump]

    for command in commands_list:
        print(f'command is executed: "{command}"')
        os.system(command)
        time.sleep(1)
