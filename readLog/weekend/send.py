# coding:utf-8

import datetime

days_send = []
days_not_send = []

rule_send = [6, 0, 1, 2, 3, 4]
rule_not_send = [4, 5]

happy_days_str = ['2017-12-30', '2017-12-31', '2018-01-01', '2018-02-15', '2018-02-16', '2018-02-17', '2018-02-18', '2018-02-19', '2018-02-20', '2018-02-21',
                   '2018-04-05', '2018-04-06', '2018-04-07',
                   '2018-04-29', '2018-04-30', '2018-05-01',
                   '2018-06-16', '2018-06-17', '2018-06-18',
                   '2018-09-22', '2018-09-23', '2018-09-24', '2018-10-01', '2018-10-02','2018-10-03','2018-10-04', '2018-10-05','2018-10-06','2018-10-07']
happy_days_str.sort()

work_days_str = ['2018-02-11', '2018-02-24', '2018-04-08', '2018-04-28', '2018-09-29', '2018-09-30']
work_days_str.sort()

for t_str in happy_days_str:
    today = datetime.datetime.strptime(t_str, '%Y-%m-%d')

    if today.weekday() in [5, 6]:
        continue

    yesterday = today - datetime.timedelta(days=1)

    if yesterday.weekday() in rule_send:
        days_not_send.append(int(yesterday.strftime('%Y%m%d')))


for t_str in work_days_str:
    today = datetime.datetime.strptime(t_str, '%Y-%m-%d')

    if today.weekday() in [0, 1, 2, 3, 4]:
        continue

    yesterday = today - datetime.timedelta(days=1)

    if yesterday.weekday() in rule_not_send:
        days_send.append(int(yesterday.strftime('%Y%m%d')))



output = {}
output["y"] = list(set(days_send))
output["n"] = list(set(days_not_send))
print output
# {"y":[20170331,20170526,20170929],"n":[20170402,20170403,20170430,20170528,20170529,20171001,20171002,20171003,20171004,20171005]}