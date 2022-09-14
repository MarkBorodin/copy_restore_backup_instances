import os
import time

from data import *


if __name__ == '__main__':

    # create 'client_data' folder
    print('mkdir client_data')
    os.system('mkdir client_data')

    # get db dump
    print(f'sudo docker exec -i {DB_CONTAINER_NAME} mysqldump -u{MYSQL_USER} -p{MYSQL_PASSWORD} --databases {MYSQL_DATABASE} --skip-comments --no-tablespaces > ./client_data/dump.sql')
    os.system(f'sudo docker exec -i {DB_CONTAINER_NAME} mysqldump -u{MYSQL_USER} -p{MYSQL_PASSWORD} --databases {MYSQL_DATABASE} --skip-comments --no-tablespaces > ./client_data/dump.sql')

    # copy from old container:
    print(f'sudo docker cp {MAUTIC_CONTAINER_NAME}:/var/www/html/app/config/local.php ./client_data/local.php')
    os.system(f'sudo docker cp {MAUTIC_CONTAINER_NAME}:/var/www/html/app/config/local.php ./client_data/local.php')

    print(f'sudo docker cp {MAUTIC_CONTAINER_NAME}:/var/www/html/media/ ./client_data/media')
    os.system(f'sudo docker cp {MAUTIC_CONTAINER_NAME}:/var/www/html/media/ ./client_data/media')

    # stop containers with removing volumes
    print(f'sudo docker-compose down -v')
    os.system(f'sudo docker-compose down -v')

    # change docker-compose.yml
    with open('docker-compose.yml', 'r') as example:
        content = example.read()
    with open('docker-compose.yml', 'w+') as docker_file:
        content = content.replace('alainmm89/automationmonkey:big-instances-latest', MAUTIC_4_IMAGE)
        docker_file.write(content)

    # rebuild docker containers
    print(f'sudo docker-compose up --build -d')
    os.system(f'sudo docker-compose up --build -d')

    time.sleep(30)

    # copy client data
    print(f'sudo docker cp ./client_data/local.php {MAUTIC_CONTAINER_NAME}:/var/www/html/app/config/local.php')
    os.system(f'sudo docker cp ./client_data/local.php {MAUTIC_CONTAINER_NAME}:/var/www/html/app/config/local.php')

    print(f'sudo docker cp ./client_data/media/dashboards/. {MAUTIC_CONTAINER_NAME}:/var/www/html/media/dashboards/.')
    os.system(f'sudo docker cp ./client_data/media/dashboards/. {MAUTIC_CONTAINER_NAME}:/var/www/html/media/dashboards/.')

    print(f'sudo docker cp ./client_data/media/images/. {MAUTIC_CONTAINER_NAME}:/var/www/html/media/images/.')
    os.system(f'sudo docker cp ./client_data/media/images/. {MAUTIC_CONTAINER_NAME}:/var/www/html/media/images/.')

    print(f'sudo docker cp ./client_data/media/files/. {MAUTIC_CONTAINER_NAME}:/var/www/html/media/files/.')
    os.system(f'sudo docker cp ./client_data/media/files/. {MAUTIC_CONTAINER_NAME}:/var/www/html/media/files/.')

    # restore db dump
    print(f'sudo docker exec -i {DB_CONTAINER_NAME} mysql -u {MYSQL_USER} -p{MYSQL_PASSWORD} {MYSQL_DATABASE} < ./client_data/dump.sql')
    os.system(f'sudo docker exec -i {DB_CONTAINER_NAME} mysql -u {MYSQL_USER} -p{MYSQL_PASSWORD} {MYSQL_DATABASE} < ./client_data/dump.sql')

    # migrations
    print(f'sudo docker exec -i {MAUTIC_CONTAINER_NAME} bash -c "php bin/console doctrine:schema:update --force"')
    os.system(f'sudo docker exec -i {MAUTIC_CONTAINER_NAME} bash -c "php bin/console doctrine:schema:update --force"')

    # docker restart
    print('sudo service docker restart')
    os.system(f'sudo service docker restart')

    # add cron-docker env vars
    print(f"""sudo docker exec -it {MAUTIC_CONTAINER_NAME} sh -c 'printenv | grep -v "no_proxy" >> /etc/environment'""")
    os.system(f'sudo docker exec -it {MAUTIC_CONTAINER_NAME} sh -c "printenv | grep -v "no_proxy" >> /etc/environment"')
