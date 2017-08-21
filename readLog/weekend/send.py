# coding:utf-8

import datetime

days_send = []
days_not_send = []

rule_send = [6, 0, 1, 2, 3, 4]
rule_not_send = [4, 5]

happy_days_strs = ['2018-01-01', '2017-08-01']
happy_days_strs.sort()

work_days_strs = []
work_days_strs.sort()

for t_str in happy_days_strs:
    today = datetime.datetime.strptime(t_str, '%Y-%m-%d')

    if today.weekday() in [5, 6]:
        continue

    yesterday = today - datetime.timedelta(days=1)

    if yesterday.weekday() in rule_send:
        days_not_send.append(int(yesterday.strftime('%Y%m%d')))


for t_str in work_days_strs:
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