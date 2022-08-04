import time
from subprocess import call
import subprocess
from data import *


if __name__ == '__main__':
    # TODO # FILL THE FILE WITH THE NECESSARY DATA AS IN THE 'data.example.py' FILE
    # command: nano data.py
    # after that run this script

    # TODO apt-get update
    print('sudo apt-get update')
    subprocess.Popen('sudo apt-get update'.split()).wait()

    # TODO install python3-pip
    print('sudo apt-get -y install python3-pip')
    subprocess.Popen('sudo apt-get -y install python3-pip'.split()).wait()

    # TODO install -r requirements.txt
    print('yes | pip install -r requirements.txt')
    subprocess.Popen('pip install -r requirements.txt'.split()).wait()

    # TODO install Docker
    print('curl -fsSL get.docker.com -o get-docker.sh')
    subprocess.Popen('curl -fsSL get.docker.com -o get-docker.sh'.split()).wait()
    print('sudo sh get-docker.sh')
    subprocess.Popen('sudo sh get-docker.sh'.split()).wait()

    # TODO install Docker-compose
    print('sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')    # noqa
    subprocess.Popen('sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'.split()).wait()    # noqa
    print('sudo chmod +x /usr/local/bin/docker-compose')
    subprocess.Popen('sudo chmod +x /usr/local/bin/docker-compose'.split()).wait()

    # TODO docker rights
    print('sudo chmod +x /usr/local/bin/docker-compose;')
    subprocess.Popen('sudo chmod +x /usr/local/bin/docker-compose;'.split()).wait()
    print('sudo usermod -aG docker $USER')
    subprocess.Popen('sudo usermod -aG docker $USER'.split()).wait()
    print('sudo chgrp docker /usr/local/bin/docker-compose')
    subprocess.Popen('sudo chgrp docker /usr/local/bin/docker-compose'.split()).wait()
    print('sudo chmod 750 /usr/local/bin/docker-compose')
    subprocess.Popen('sudo chmod 750 /usr/local/bin/docker-compose'.split()).wait()

    # TODO download data
    print('download_from_s3.py')
    exec(open("download_from_s3.py").read())

    # TODO add_cron_jobs
    print('sudo python3 add_cron_jobs.py')
    subprocess.Popen('sudo python3 add_cron_jobs.py'.split()).wait()

    # TODO create and run docker-compose.yml
    print('create_docker_compose_file.py')
    exec(open("create_docker_compose_file.py").read())
    print('sudo docker-compose up --build -d')
    subprocess.Popen('docker-compose up --build -d'.split()).wait()

    time.sleep(10)

    # TODO restore from dump
    print('restore_from_copy.py')
    exec(open("restore_from_copy.py").read())

    time.sleep(10)

    # TODO cron-docker env vars
    print(f'docker exec -it {MAUTIC_CONTAINER_NAME} sh -c "printenv | grep -v "no_proxy" >> /etc/environment"')
    subprocess.Popen(f'sudo docker exec -it {MAUTIC_CONTAINER_NAME} sh -c "printenv | grep -v "no_proxy" >> /etc/environment"'.split()).wait()    # noqa

    # TODO Apache
    print('sudo apt -y install apache2')
    subprocess.Popen('sudo apt -y install apache2'.split()).wait()
    print('echo "y" | sudo ufw allow "Apache"')
    subprocess.Popen('sudo ufw allow "Apache"'.split()).wait()
    print('echo "y" | sudo ufw allow "Apache Full"')
    subprocess.Popen('sudo ufw allow "Apache Full"'.split()).wait()
    print('echo "y" | sudo ufw allow ssh')
    subprocess.Popen('sudo ufw allow ssh'.split()).wait()
    print('sudo ufw enable')
    subprocess.Popen('sudo ufw enable'.split()).wait()

    print('edit mautic.conf')
    with open('mautic.conf', 'r') as file:
        file_data = file.read()
    file_data = file_data.replace('your_url', NEW_URL.replace('https://', '').replace('http://', ''))
    with open('mautic.conf', 'w') as file:
        file.write(file_data)

    print('sudo cp ./mautic.conf /etc/apache2/sites-available/mautic.conf')
    subprocess.Popen('sudo cp ./mautic.conf /etc/apache2/sites-available/mautic.conf'.split()).wait()
    print('sudo a2ensite mautic.conf')
    subprocess.Popen('sudo a2ensite mautic.conf'.split()).wait()
    print('sudo a2enmod rewrite')
    subprocess.Popen('sudo a2enmod rewrite'.split()).wait()
    print('sudo a2enmod proxy')
    subprocess.Popen('sudo a2enmod proxy'.split()).wait()
    print('sudo a2enmod proxy_http')
    subprocess.Popen('sudo a2enmod proxy_http'.split()).wait()
    print('sudo a2enmod proxy_balancer')
    subprocess.Popen('sudo a2enmod proxy_balancer'.split()).wait()
    print('sudo a2enmod lbmethod_byrequests')
    subprocess.Popen('sudo a2enmod lbmethod_byrequests'.split()).wait()
    print('sudo service apache2 restart')
    subprocess.Popen('sudo service apache2 restart'.split()).wait()

    # TODO Certificate
    print('sudo apt -y install certbot python3-certbot-apache')
    subprocess.Popen('sudo apt install certbot python3-certbot-apache'.split()).wait()
    # print('sudo certbot --non-interactive --apache --agree-tos -m {CERTBOT_EMAIL} -d {NEW_URL}')
    # subprocess.Popen(f'sudo certbot --non-interactive --apache --agree-tos -m {CERTBOT_EMAIL} -d {NEW_URL}'.split()).wait()    # noqa
