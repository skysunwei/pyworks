# for line in open('goodtuanzhang'):
#     tuanzhang = line.strip('\n').split(',')
#     # print tuanzhang[0] + tuanzhang[1]
#     print 'MAX( CASE a.`recommenduserid` WHEN ' + tuanzhang[0] +' THEN money ELSE 0 END ) ' + tuanzhang[1] + ','

qus = {}
current_qu = ''

for line in open('store'):
    store = line.strip('\n').split(',')
    print 'insert `op-sunwei-store-mapping`(`merchtypeid`,`code`) values(%s, \'%s\');' % \
          (store[0], store[1])

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
#         print 'insert `district`(`title`,`level`,`usetype`,`parentid`,`deleted`) values(\'' + qu + '\',3, 0, ' + qus[current_qu] + ', 0);'
#         # break


