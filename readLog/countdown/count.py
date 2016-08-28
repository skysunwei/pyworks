__author__ = 'colin'

import datetime

deadline = '2017-07-26'

current_time = datetime.datetime.now()

print current_time

time_interval = datetime.datetime.strptime(deadline, "%Y-%m-%d") - current_time

days_num = time_interval.days
days_every = round(float(days_num) / 166)

print days_every