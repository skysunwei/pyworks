#-*- coding: UTF-8 -*-

import dbSource

dbSource.mysql_connect()

error_lines = []

for line in open('new_tuanzhang'):
    tuanzhangs = line.split(',')

    result_line = ''

    try:

        for tz in tuanzhangs:
            nickname = tz.strip('\n')

            sql = 'SELECT `userweixin`.`userid` FROM `userweixin`, `saler` WHERE' \
                  '`userweixin`.`userid` = `saler`.`userid` AND `nickname` LIKE \'' + nickname + '\''

            user_id = dbSource.mysql_query(sql)
            result_line += str(user_id.rows[0][0]) + ','

        print result_line
    except:
        # print nickname + ' 找不到!'
        error_lines.append(line)


dbSource.mysql_close()

for er in error_lines:
    print er.strip('\n')