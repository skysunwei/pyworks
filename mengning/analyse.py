# coding: utf-8

import re


def read_log_file(log_file, day):

    output = open('data.sql', 'w')
    sqls = []

    for line in open(log_file):

        try:
            str_time = re.findall(r"\[(.+?)\]", line)[0]

            temp_datas = re.findall(r"{(.+?)}", line)
            view_info = temp_datas[0].split(',')
            user_info = temp_datas[1].split(',')

            user_id = int(view_info[0].split(':')[1].strip('"'))
            url = view_info[1].split(':', 1)[1].strip('"')
            client = view_info[2].split(':')[1].strip('"')
            user_nickname = user_info[1].split(':')[1].strip('"')

            if str_time.find(day) is 0:

                sql = 'INSERT INTO view(userId, url, client, dateline, day) ' \
                      'VALUES(%s, \'%s\', \'%s\', \'%s\', \'%s\');' \
                      % (user_id, url, client, str_time, day)

                sqls.append(sql)

        except Exception, e:
            print Exception, ":", e
            print line
            # break

    output.writelines(sqls)

    output.close()

read_log_file('201706.log', '2017-06-03')
