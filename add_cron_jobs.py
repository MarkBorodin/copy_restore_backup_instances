from crontab import CronTab
from data import *


if __name__ == '__main__':
    cron = CronTab(user=OS_USER)

    # renew certbot
    job1 = cron.new(command="/usr/bin/certbot renew --quiet >> /var/log/mycronjob.log 2>&1")
    job1.setall('5 12 * * *')
    cron.write()

    # remove_old_copies_from_s3
    job2 = cron.new(command="cd ~ && python3 remove_old_copies_from_s3.py >> /var/log/mycronjob.log 2>&1")
    job2.setall('10 12 * * *')
    cron.write()

    # get_copy_and_dump
    job3 = cron.new(command="cd ~ && python3 get_copy.py >> /var/log/mycronjob.log 2>&1")
    job3.setall('15 12 * * *')
    cron.write()
