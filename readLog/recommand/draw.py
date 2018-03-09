# coding:utf-8

import csv

source_file_name = 'saler.csv'

saler_guwens = {27997: 69, 38617: 70, 67413: 71, 145007: 72, 48416: 73, 89159: 74, 237: 75, 81560: 76}

lines = []

vips = []

payorders = {}

relations = {}
root_relations = {}

source_file = csv.reader(file(source_file_name, 'rb'))
for the_line in source_file:
    lines.append(the_line)


def read():
    for line in lines:
        id = int(line[0])
        pid = int(line[1])

        try:
            order_num = int(line[2])
        except:
            order_num = 0

        if id not in payorders.keys():
            payorders[id] = order_num

        if pid not in relations.keys():
            relations[pid] = []
            relations[pid].append(id)
        else:
            relations[pid].append(id)

        try:
            is_vip = int(line[3])
            if is_vip == 1:
                vips.append(id)
        except:
            continue


def root():
    ids = []
    pids = []

    for line in lines:
        id = int(line[0])
        pid = int(line[1])

        ids.append(id)
        pids.append(pid)

    root_salers = [i for i in pids if i not in ids]
    root_salers = list(set(root_salers))
    root_salers.sort()

    return root_salers


def size():
    for line in lines:
        id = int(line[0])
        pid = int(line[1])

        if id in relations.keys() and pid in relations.keys():
            if pid not in root_relations.keys():
                root_relations[pid] = []
                root_relations[pid].append(id)
            else:
                root_relations[pid].append(id)


read()
root()
size()

# def calculate(root_saler_id):

#
#     datas = []
#
#     if root_saler_id in root_relations.keys():
#         for saler in root_relations[root_saler_id]:
#             datas.extend(calculate(saler))
#
#         for saler in list(set(relations[root_saler_id])^set(root_relations[root_saler_id])):
#             datas.extend(calculate(saler))
#
#         return datas
#     else:
#         if root_saler_id in relations.keys():
#             return relations[root_saler_id]
#         else:
#             return [root_saler_id]


def calculate(root_saler_id):
    datas = [root_saler_id]
    if root_saler_id in relations.keys():
        for saler in relations[root_saler_id]:
            datas.extend(calculate(saler))
        return datas
    else:
        return [root_saler_id]

# print vips

f = file('output.csv', "w+")

f.writelines('guwenID, zxsID \n')

for gonghuizhang in saler_guwens.keys():

    all_zxs = calculate(gonghuizhang)
    intersection = [v for v in all_zxs if v in vips]

    for vip_zxs in intersection:
        f.writelines(str(saler_guwens[gonghuizhang]) + ',' + str(vip_zxs) + '\n')

f.close()

print 'done'

exit()




def sum_orders(list):
    a = 0
    for l in list:
        a += payorders[l]
    return a


def count_orders(k):
    if root_relations.has_key(k):
        i = 0
        # print relations[k]
        # print k, sum_orders(relations[k]), relations[k]
        # print i
        for saler in root_relations[k]:
            i = i + count_orders(saler)
            # print i
        return sum_orders(relations[k]) + i
    else:
        if k in relations:
            # print k
            return sum_orders(relations[k])
        else:
            return 0

print calculate(1916)

# # for k in root():
# #     print k, ',', calculate(k), ',', count_orders(k)
#
# f = file('output.csv', "w+")
#
# for line in lines:
#     userid = int(line[0])
#     data = '%s,%s,%s\n' % (userid, calculate(userid), count_orders(userid))
#     f.writelines(data)
#
# for userid in root():
#     data = '%s,%s,%s\n' % (userid, calculate(userid), count_orders(userid))
#     f.writelines(data)
#
# f.close()
#
# print 'done'
