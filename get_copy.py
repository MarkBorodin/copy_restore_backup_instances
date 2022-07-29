import os
import time
from datetime import datetime
import shutil

from data import *

# COMMANDS
get_volume = f'docker cp {MAUTIC_CONTAINER_NAME}:/var/www/html ./snapshot/'
get_db_dump = f'docker exec -i {DB_CONTAINER_NAME} mysqldump -u{MYSQL_USER} -p{MYSQL_PASSWORD} --databases {MYSQL_DATABASE} --skip-comments --no-tablespaces > ./snapshot/dump.sql'  # noqa

commands_list = [get_volume, get_db_dump]


if __name__ == '__main__':

    for command in commands_list:
        print(f'command is executed: "{command}"')
        os.system(command)
        time.sleep(1)

    shutil.make_archive(f'./{datetime.today().strftime("%d.%m.%Y")}', 'zip', './snapshot')
    shutil.rmtree('./snapshot')
