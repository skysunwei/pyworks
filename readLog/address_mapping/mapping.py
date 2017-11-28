#-*- coding: UTF-8 -*-

import csv

citys = {}
districts = {}
district_names = {}

folder_name = 'chongqing/'
province_name = '重庆市'
provinceid = '22'
file_name = folder_name + 'chongqing.csv'

for line in open(folder_name + 'city.txt'):
    datas = line.strip('\n').split(',')
    citys[datas[0]] = datas[1]

for line in open(folder_name + 'district.txt'):
    datas = line.strip('\n').split(',')
    districts[datas[0]] = datas[1]
    district_names[datas[0]] = datas[2]


csvfile = file(file_name, 'rb')
reader = csv.reader(csvfile)


def remove_old(inputs):

    inputs = inputs.replace(province_name, '').replace(province_name, '')

    for x in citys.values():
        inputs = inputs.replace(x, '')
        inputs = inputs.replace(x.replace('市', ''), '')

    for x in districts.values():
        inputs = inputs.replace(x, '')
        inputs = inputs.replace(x.replace('市', ''), '')

    return inputs


print 'addressid,province,city,district,address'
for line in reader:

    try:
        print line[0] + ',' + provinceid + ',' + line[3] + ',' + districts[line[3]], ',' + province_name + citys[line[3]] + district_names[line[3]] + remove_old(line[4])
    except:
        # if line[1] != '5028':
        #     print line[0], line[3]
        print


#
# rule = {}
# source = {}
#
# for t in range(41, 51):
#     rule[t] = []
#
# # print rule
#
#
# for line in open('district'):
#     districts = line.strip('\n').split(',')
#
#     kv = {}
#     kv[districts[2]] = districts[0]
#     # print kv
#     rule[int(districts[1])].append(kv)
#
# # for i in range(41, 51):
# #     print len(rule[i])
# #     for j in range(len(rule[i])):
# #         print rule[i][j]
#
# for line in open('source'):
#     sources = line.strip('\n').split(',')
#
#     key = int(sources[1])
#     # print key
#
#     if key in rule.keys():
#         # print key
#         for j in range(len(rule[key])):
#             # print rule[key][j]
#             # print sources[3]
#
#             try:
#                 if sources[3] in rule[key][j].keys():
#                     print 'update `recipientaddress` set `district`=', \
#                         rule[key][j][sources[3]] ,' where `addressid`=', sources[0],';'
#                     # break
#                 # else:
#                     # print line
#                     # print 'not in'
#             except Exception,e:
#                 # print line
#                 # print Exception, ':', e
#                 break
