from subprocess import call

if __name__ == '__main__':
    # # TODO # FILL THE FILE WITH THE NECESSARY DATA AS IN THE 'data.example.py' FILE
    # # command: nano data.py
    # # after that run this script

    # # RUN 'sudo apt-get update'
    # call('sudo apt-get update', shell=True)

    # # RUN 'sudo apt-get -y install python3-pip'
    # call('sudo apt-get -y install python3-pip', shell=True)

    # # RUN 'pip install -r requirements.txt'
    # call('pip install -r requirements.txt', shell=True)

    # # - Install Docker (https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)   # noqa
    # ...

    # # - Install Docker-compsoe (https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)   # noqa
    # ...

    # # git clone repository
    # call('git clone https://github.com/MarkBorodin/copy_restore_backup_instances.git', shell=True)
    # call('cp ./copy_restore_backup_instances/* ~/.', shell=True)



    # TODO download data
    exec(open("download_from_s3.py").read())
    # TODO check and delete if > 30 day
    exec(open("add_cron_jobs.py").read())
    # TODO create and run docker-compose.yml
    # TODO restore from dump
    exec(open("restore_from_copy.py").read())
    # TODO Apache
    # TODO DNS
    # TODO Certificate

