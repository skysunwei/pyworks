import dbSource


def read_log_file(log_file, day):
    dbSource.mysql_connect()

    for line in open(log_file):

        try:
            x = line.split('[')
            str_time = (x[1].split(']'))[0]
            data = (x[2].split(']'))[0].split(',"')
            userId = data[0].strip('"')
            client = data[2].strip('"')
            url = data[1].strip('"')

            if str_time.find(day) is 0:
                sql = 'INSERT INTO view(userId, url, client, dateline, day) ' \
                      'VALUES(%s, \'%s\', \'%s\', \'%s\', \'%s\');' \
                      % (userId, url, client, str_time, day)

                dbSource.mysql_query(sql)
        except:
            print line
    dbSource.mysql_close()


read_log_file('201611.log', '2016-11-20')
