# coding:utf-8


# for line in open('test'):
#     datas = line.strip('\n').split(',')
#     # print
#     sql = 'update `youhaodongxi`.`saler` set `dateline`=%s where `userid`=%s;' % (datas[1], datas[0])
#     print sql


# for line in open('test'):
#     datas = line.strip('\n')
#     show = '{"company": "1002", "time": "12,17,22", "city": "%s"},' % datas
#     print show

# jiuye = []
#
# notin = []
#
# for line in open('jiuye'):
#     jiuye.append(line.strip('\n'))
#
# for line in open('higo'):
#     datas = line.strip('\n').split(',')
#
#     if datas[1] not in jiuye:
#         notin.append(datas[1])
#
# print notin
#
# for line in open('higo'):
#     datas = line.strip('\n').split(',')
#
#     if datas[1] in notin:
#         print datas[0]

# nav = []
#
# for line in open('nav'):
#     nav.append(line.strip('\n'))
#
# express = {}
#
# for line in open('express'):
#     datas = line.strip('\n').split(',')
#
#     express[datas[0]] = datas[1]
#
# send = {}
#
# for line in open('higo'):
#     datas = line.strip('\n').split(',')
#
#     if datas[0] == 173940:
#         continue
#
#     if datas[0] in nav:
#         send[datas[0]] = datas[1]
#
#         sql = 'update `youhaodongxi`.`express` set `expressno`=\'%s\',`companycode`=\'%s\',`company`=\'%s\' ' \
#               'where `expressid`=%s;' % (datas[1], 'pjbest', '品骏', express[datas[0]])
#
#         print sql

for line in open('test1.txt'):
    UPDATE
    `ticket`
    SET
    ticket.
    `onsale` = 3
    WHERE
    ticket.
    `ticketseatid`
    IN(select
    ticketseat.
    `ticketseatid`
    from ticketseat where

    ticketseat.
    `description` = '1层14排3座'
    )

    print line

# print len(send)

#
# for k in send.keys():
#     print k, send[k]

# i = 0
#
# for line in open('test1.txt'):
#     datas = line.strip('\n').split(',')
#
#     i += 1
#
#     for data in datas:
#         sql = 'update `youhaodongxi`.`merchandise` set `recommendlayoutid`=%s where `merchandiseid`=%s;' % (i, data)
#         print sql


# import json
#
# for line in open('test'):
#     datas = line.strip('\n').split(',')
#
#     output = {}
#     output['107'] = {}
#     output['108'] = {}
#
#     if datas[2] is '1':
#         type = {}
#         type['2'] = ''
#         type['3'] = 3
#         type['4'] = 3
#
#         output['107']['3'] = type
#         output['108']['3'] = type
#
#     if datas[2] is '2':
#         type = {}
#         type['2'] = datas[1]
#         type['3'] = 3
#         type['4'] = 3
#
#         output['107']['2'] = type
#         output['108']['2'] = type
#
#     sql = 'update `youhaodongxi`.`merchandise` set `despatchtype`=\'%s\' where ' \
#           '`merchandiseid`=%s;' % (json.dumps(output), datas[0])
#
#     print sql



    # if datas[2] is '2':


    #
    # for line in open('test'):
    #     datas = line.strip('\n').split(',')
    #     # print
    #     vars = datas[1].split('a:5:')[1].split(';')
    #
    #     print datas[0], ',', \
    #         int(vars[9].split(':')[2])/100, ',', \
    #         vars[3].split(':')[1], ',', \
    #         vars[5].split(':')[1]




    # split = datas[1].split(',')
    #
    # for i in split:
    #     if 'amount' in i:
    #         # print i
    #         print datas[0], ',', i.split(':')[1]


    # sql = 'update `merchandise` set `quantity`=%s where `merchandiseid`=%s;' % (datas[2], datas[1])


# higo = []
#
# for line in open('higo'):
#     higo.append(line.strip('\n'))
#
# for line in open('yhdx'):
#     if line.strip('\n') not in higo:
#         print line

# controllers = {}

# for line in open('nav'):
#
#     data = line.strip('\n').split(',')
#     urls = data[1].split('/')
#     keyword = urls[-2]
#
#     if keyword not in controllers.keys():
#         controllers[keyword] = []
#     controllers[keyword].append(line)
#     # print data[0]
#     # print keyword
#
# for k in controllers:
#     print k
#     for i in controllers[k]:
#         print '     ' + i
