#-*- coding: UTF-8 -*-

import dbSource
import codecs


WHERE_DELETED_AND_LEVEL_ = 'SELECT `districtid`, `title` FROM `district` WHERE `deleted` = 0 AND `level` = '


shengShi = {}
shiQu = {}

dbShengShi = {}
dbShiQu = {}

zhiXiaShi = []


def print_map_value(map):
    for keys in map.keys():
        show = ''
        for item in map[keys]:
            show += item + ',';
        print ("key:%s Value: %s" % (keys, show))


def read_zhixiashi():
    for line in codecs.open('zhixiashi.txt', 'r', 'utf-8'):
        zhiXiaShi.append(line.strip('\n'))


def read_db():
    dbSource.mysql_connect()

    sql = WHERE_DELETED_AND_LEVEL_ + '1'
    dbShens = dbSource.mysql_query(sql)


    for dbShen in dbShens.rows:
        sql = WHERE_DELETED_AND_LEVEL_ + '2 AND `parentid` = ' + str(dbShen[0])
        dbShis = dbSource.mysql_query(sql)

        dbShengShi[dbShen[1]] = []
        for dbShi in dbShis.rows:
            dbShengShi[dbShen[1]].append(dbShi[1])

            sql = WHERE_DELETED_AND_LEVEL_ + '3 AND `parentid` = ' + str(dbShi[0])
            dbQus = dbSource.mysql_query(sql)

            dbShiQu[dbShi[1]] = []
            for dbQu in dbQus.rows:
                dbShiQu[dbShi[1]].append(dbQu[1])

    # print_map_value(dbShengShi)
    # print_map_value(dbShiQu)

    dbSource.mysql_close()


def read_good():
    province = ''
    city = ''
    count = 0

    for line in codecs.open('shiqu.txt', 'r', 'utf-8'):

        try:
            key_value = line.strip('\n').split('	')
            key = int(key_value[0])
            value = key_value[1]

            if key % 10000 == 0:
                if province != value:
                    province = value
                    shengShi[province] = []

                if value in zhiXiaShi:
                    # print '直辖市'
                    city = value
                    shiQu[city] = []
                    shengShi[province].append(city)

                continue

            if key % 100 == 0:
                if city != value:
                    city = value
                shiQu[city] = []
                shengShi[province].append(city)
                continue

            if key % 100 > 0:
                district = value
                shiQu[city].append(district)
        except:
            print line

    # print_map_value(shengShi)
    # print_map_value(shiQu)


def compare_cities():

    for (key, value) in shengShi.items():
        diff = set(value).difference(dbShengShi[key])

        for item in diff:
            print key + ',' + item


def compare_districts():

    for (key, value) in shiQu.items():
        if key not in dbShiQu:
            print key
            continue

        diff = set(value).difference(set(dbShiQu[key]))

        for item in diff:
            # print key + ',' + item
            # print item
            # del_qu_sql = 'UPDATE `district` SET `deleted` = 1 WHERE `level` = 3 AND `title` = \''+ item + '\';'
            # print del_qu_sql

            insert_qu_sql = 'INSERT INTO district (title,`level`,parentid, usetype,deleted) select \'' + \
                            item + '\',3, districtid, 3, 0 FROM district where deleted = 0 and title = \'' + key + '\';'
            print insert_qu_sql



read_zhixiashi()
read_db()
read_good()
# compare_cities()
compare_districts()