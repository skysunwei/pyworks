# coding:utf-8

import json

print '渠道,金额,张数,优惠券编号'

for line in open('test'):
    datas = line.strip('\n').split(',')
    # print
    vars = datas[1].split('a:5:')[1].split(';')

    print datas[0], ',', \
        int(vars[9].split(':')[2])/100, ',', \
        vars[3].split(':')[1], ',', \
        vars[5].split(':')[1]

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
