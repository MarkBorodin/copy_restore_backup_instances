import time
from subprocess import call
import subprocess
from data import *


if __name__ == '__main__':
    ...
    # TODO # FILL THE FILE WITH THE NECESSARY DATA AS IN THE 'data.example.py' FILE
    # command: nano data.py
    # after that run this script

    # TODO apt-get update
    subprocess.Popen('sudo apt-get update'.split()).wait()

    # TODO install python3-pip
    subprocess.Popen('sudo apt-get -y install python3-pip'.split()).wait()

    # TODO install -r requirements.txt
    subprocess.Popen('pip install -r requirements.txt'.split()).wait()

    # TODO install Docker
    subprocess.Popen('curl -fsSL get.docker.com -o get-docker.sh'.split()).wait()
    subprocess.Popen('sudo sh get-docker.sh'.split()).wait()

    # TODO install Docker-compose
    subprocess.Popen('sudo sh install-docker-compose.sh'.split()).wait()

    # TODO clone repository
    # subprocess.Popen('git clone https://github.com/MarkBorodin/copy_restore_backup_instances.git'.split()).wait()
    # subprocess.Popen('cp ./copy_restore_backup_instances/* ~/.'.split()).wait()

    # TODO download data
    exec(open("download_from_s3.py").read())

    # TODO add_cron_jobs
    exec(open("add_cron_jobs.py").read())

    # TODO create and run docker-compose.yml
    exec(open("create_docker_compose_file.py").read())
    subprocess.Popen('docker-compose up --build -d'.split()).wait()

    time.sleep(10)

    # TODO restore from dump
    exec(open("restore_from_copy.py").read())

    time.sleep(10)

    # TODO cron-docker env vars
    subprocess.Popen('docker exec -ti my_container sh -c "printenv | grep -v "no_proxy" >> /etc/environment"'.split()).wait()    # noqa

    # TODO Apache
    subprocess.Popen('sudo apt -y install apache2'.split()).wait()
    subprocess.Popen('sudo ufw allow "Apache"'.split()).wait()
    subprocess.Popen('sudo ufw allow "Apache Full"'.split()).wait()
    subprocess.Popen('sudo ufw allow ssh'.split()).wait()
    subprocess.Popen('sudo ufw enable'.split()).wait()

    with open('mautic.conf', 'r') as file:
        file_data = file.read()
    file_data = file_data.replace('your_url', NEW_URL.replace('https://', '').replace('http://', ''))
    with open('mautic.conf', 'w') as file:
        file.write(file_data)

    subprocess.Popen('sudo cp ./mautic.conf /etc/apache2/sites-available/mautic.conf'.split()).wait()
    subprocess.Popen('sudo a2ensite mautic.conf'.split()).wait()
    subprocess.Popen('sudo a2enmod rewrite'.split()).wait()
    subprocess.Popen('sudo a2enmod proxy'.split()).wait()
    subprocess.Popen('sudo a2enmod proxy_http'.split()).wait()
    subprocess.Popen('sudo a2enmod proxy_balancer'.split()).wait()
    subprocess.Popen('sudo a2enmod lbmethod_byrequests'.split()).wait()
    subprocess.Popen('sudo service apache2 restart'.split()).wait()

    # TODO Certificate
    subprocess.Popen('sudo apt install certbot python3-certbot-apache'.split()).wait()
    # subprocess.Popen(f'sudo certbot --non-interactive --apache --agree-tos -m {CERTBOT_EMAIL} -d {NEW_URL}'.split()).wait()    # noqa
