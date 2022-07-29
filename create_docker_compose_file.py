from data import *

with open('docker-compose-example.yml', 'r') as example:
    with open('docker-compose.yml', 'w+') as docker_file:
        content = example.read()
        content = content.replace('DB_CONTAINER_NAME_EXAMPLE', DB_CONTAINER_NAME)
        content = content.replace('MYSQL_ROOT_PASSWORD_EXAMPLE', MYSQL_ROOT_PASSWORD)
        content = content.replace('MYSQL_DATABASE_EXAMPLE', MYSQL_DATABASE)
        content = content.replace('MYSQL_USER_EXAMPLE', MYSQL_USER)
        content = content.replace('MYSQL_PASSWORD_EXAMPLE', MYSQL_PASSWORD)
        content = content.replace('MAUTIC_CONTAINER_NAME_EXAMPLE', MAUTIC_CONTAINER_NAME)
        docker_file.write(content)
