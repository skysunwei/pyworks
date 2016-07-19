import dbSource
import os.path

rootdir = "frontroute"

dbSource.mysql_connect()

for parent, dirNames, filenames in os.walk(rootdir):
    for filename in filenames:
        print os.path.join(parent,filename)

        for line in open(os.path.join(parent,filename)):

            try:
                x = line.split('[')
                time = (x[1].split(']'))[0]
                data = (x[2].split(']'))[0].split(',"')

                userId = data[0].strip('"')
                url = data[1].strip('"')
                client = data[2].strip('"')

                sql = 'INSERT INTO view(userId, url, client, dateline) VALUES(' + userId + ',"' + url + '","' + client + '","' + time + '");'

                dbSource.mysql_query(sql)
            except:
                print parent,filename
                print line

dbSource.mysql_close()