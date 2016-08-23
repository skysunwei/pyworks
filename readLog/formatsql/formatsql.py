#-*- coding: UTF-8 -*-

# for line in open('goodtuanzhang'):
#     tuanzhang = line.strip('\n').split(',')
#     # print tuanzhang[0] + tuanzhang[1]
#     print 'MAX( CASE a.`recommenduserid` WHEN ' + tuanzhang[0] +' THEN money ELSE 0 END ) ' + tuanzhang[1] + ','

qus = {}
current_qu = ''


def insert_sql():
    for line in open('store'):
        store = line.strip('\n').split(',')
        print 'insert `op-sunwei-store-mapping`(`merchtypeid`,`code`) values(%s, \'%s\');' % \
              (store[0], store[1])


def update_sql():
    i = 1

    for line in open('wrongkuaidi'):
        exp = line.strip('\n').split(',')
        print 'update express, paysuborder set express.expressno = \'%s\', ' \
              '`express`.`company` = \'中通快递\', `express`.`companycode` = \'zhongtong\' ' \
              'where express.expressid = paysuborder.expressid ' \
              'and `paysuborder`.suborderid = %s;' % \
              (exp[1], exp[0])
        i += 1

update_sql()

# print qus.keys()
# for line in open('newqu'):
#     qu = line.strip('\n')
#
#     if qu == '':
#         continue
#
#     if qu in qus.keys():
#         current_qu = qu;
#     else:
#         print 'insert `district`(`title`,`level`,`usetype`,`parentid`,`deleted`)
# values(\'' + qu + '\',3, 0, ' + qus[current_qu] + ', 0);'
#         # break
