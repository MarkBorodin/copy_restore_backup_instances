if __name__ == '__main__':
    with open('/etc/crontab', 'a') as fd:
        fd.write(f'\n5 12 * * * root /usr/bin/certbot renew --quiet >> /var/log/mycronjob.log 2>&1')
        fd.write(f'\n10 12 * * * root cd ~ && python3 remove_old_copies_from_s3.py >> /var/log/mycronjob.log 2>&1')
        fd.write(f'\n15 12 * * * root cd ~ && python3 get_copy.py >> /var/log/mycronjob.log 2>&1')
