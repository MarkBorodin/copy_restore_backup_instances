### copy and unpack repository:   
git clone https://github.com/MarkBorodin/copy_restore_backup_instances.git   
cp ./copy_restore_backup_instances/* ~/.   

### create and fill in data.py file as in data.example.py file:   
nano data.py
  
### run script:   
sudo python3 install.py   

### update cronjobs
sudo nano /etc/crontab
ctrl + o
enter
ctrl + x

### reload cron:   
sudo service cron reload

### reload docker:   
sudo systemctl restart docker

### set env vars for cron in docker:   
sudo docker exec -it automationmonkey_latest sh -c "printenv | grep -v "no_proxy" >> /etc/environment"

***

Copy repository and unpack folder to the working directory.
Create and fill in data.py file as in data.example.py file
Run script install.py.
The data will be taken from the data.py file.

You may need to press "enter" several times during the installation process.

there will be installed: pip, all from requirements.txt, docker, docker-compose, apache, certbot
The archive from s3 will be downloaded. The archive must have a .zip extension. The archive must be a snapshot of the mautic instance and must contain the file dump.sql - a dump of the database of the mautic instance.
A docker-compose file will be created and 2 containers will be launched. They will be restored with downloaded and unpacked data and files from s3 (restoring instance)
Apache will be installed, configured and started
The sertbot will be installed and the certificate will be obtained

Cron jobs will be added for:
- daily creation of a database dump and a snapshot of an instance. The created archive will be uploaded to s3 into a folder whose name will be defined in the INSTANCE_NAME variable from the data.py file.
- checking the s3 storage and deleting copies that are more than 30 days old.
- certificate renewal

there will be executed the command which needed to pass variables from docker to cron in container.

***

The files from this set of scripts can also be used individually. For example download\upload\delete files from s3. (there are several videos about it)
download_from_s3.py
upload_to_s3_bucket.py
delete_from_s3.py
To do this, it is needed to pass key arguments to the corresponding method in the corresponding file:
"key" - the key to the file on s3. By default, it will be formed from the INSTANCE_NAME and UPLOAD_S3_KEY\DOWNLOAD_S3_KEY variables from the data.py file. You can specify your key directly in the desired file and method, or change the specified variables in the data.py file. "key" example: 'marketeersbern/28.07.2022.zip'
"filename" - the name of the downloaded file. The default is the same as UPLOAD_S3_KEY\DOWNLOAD_S3_KEY. It is possible to enter your own filename.




