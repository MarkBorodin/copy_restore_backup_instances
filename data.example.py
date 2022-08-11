from datetime import datetime


# ***********************************************
# DOCKER

# Database container name
DB_CONTAINER_NAME: str = 'automationmonkey_db'

# mysql root password
MYSQL_ROOT_PASSWORD: str = 'some password'

# mysql database name
MYSQL_DATABASE: str = 'some db name'

# mysql user name
MYSQL_USER: str = 'some name'

# mysql password
MYSQL_PASSWORD: str = 'some password'

# database container name
MAUTIC_CONTAINER_NAME: str = 'automationmonkey_latest'
# ***********************************************


# ***********************************************
# AWS

# AWS_ACCESS_KEY_ID
AWS_ACCESS_KEY_ID: str = 'some key'

# AWS_SECRET_ACCESS_KEY
AWS_SECRET_ACCESS_KEY: str = 'some key'

# S3_BUCKET NAME
S3_BUCKET: str = 'some name'

# UPLOAD S3_FILENAME S3_KEY (generated automatically - today's date + .zip)
UPLOAD_S3_FILENAME: str = datetime.today().strftime("%d.%m.%Y") + '.zip'

# UPLOAD_S3_FILENAME
UPLOAD_S3_KEY: str = UPLOAD_S3_FILENAME

# DOWNLOAD S3_FILENAME S3_KEY (generated automatically - today's date + .zip)
DOWNLOAD_S3_FILENAME: str = datetime.today().strftime("%d.%m.%Y") + '.zip'

# DOWNLOAD_S3_FILENAME
DOWNLOAD_S3_KEY: str = DOWNLOAD_S3_FILENAME
# ***********************************************


# ***********************************************
# GENERAL

# instance name (is part of the key for basket s3. (folder name))
INSTANCE_NAME: str = 'test'

# os user
OS_USER: str = 'ubuntu'

# certificate renewal email
CERTBOT_EMAIL: str = 'some@hotmail.com'
# ***********************************************


# ***********************************************
# MAUTIC

# Old url
OLD_URL: str = 'http://127.0.0.1:8080'

# New url
NEW_URL: str = 'http://127.0.0.1:8080'

# Username
USER_NAME: str = 'some username'

# User password
USER_PASSWORD: str = 'some password'
# ***********************************************
