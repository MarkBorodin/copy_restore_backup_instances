if __name__ == '__main__':
    with open('/etc/crontab', 'a') as fd:
        fd.write(f'\n5 12 * * * root /usr/bin/certbot renew --quiet >> /var/log/mycronjob.log 2>&1')
        fd.write(f'\n10 12 * * * root cd /home/ubuntu && python3 /home/ubuntu/remove_old_copies_from_s3.py >> /var/log/mycronjob.log 2>&1')    # noqa
        fd.write(f'\n15 12 * * * root cd /home/ubuntu && python3 /home/ubuntu/get_copy.py >> /var/log/mycronjob.log 2>&1')    # noqa
        fd.write(f'\n20 12 * * * root cd /home/ubuntu && python3 /home/ubuntu/upload_to_s3_bucket.py >> /var/log/mycronjob.log 2>&1')    # noqa
