import dbSource
import json


dbSource.mysql_connect()

SEARCH = 'SELECT `title` FROM `district` WHERE `districtid` = '

area = open('area').read()
data_string = json.loads(area)

beijing = data_string['1']

for k in beijing.keys():

    sql = SEARCH + k
    print dbSource.mysql_query(sql).rows[0][0]

    for v in beijing[k]:
        sql = SEARCH + str(v)
        print '[', dbSource.mysql_query(sql).rows[0][0], ']'

    # print k, '', beijing[k]
