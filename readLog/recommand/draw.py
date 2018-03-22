# coding:utf-8

import csv

source_file_name = 'payorder.csv'

#saler_guwens = {27997: 69, 38617: 70, 67413: 71, 145007: 72, 48416: 73, 89159: 74, 237: 75, 81560: 76}

# saler_guwens = {27997: '星星', 38617: '王哲君', 67413: '笑笑', 145007: '小颖', 48416: '靖', 89159: '建新', 237: '赵影', 81560: '峥'}

saler_guwens = {237: '赵影', 1167969: '白夜', 832631: '赵影',1199916: '赵影',671652: '赵影',1196675: '赵影',205591: '赵影',249008: '赵影',116331: '赵影',172146: '赵影',662782: '赵影',315755: '赵影',453944: '赵影',614297: '赵影',182797: '赵影',1229910: '赵影',448600: '赵影',903071: '赵影',223835: '赵影',837491: '赵影',884846: '赵影',820274: '赵影',4331: '赵影',840989: '赵影',1190862: '赵影',1189790: '赵影',1210048: '赵影',1116989: '赵影',208583: '赵影',1183059: '赵影',654652: '赵影',925336: '赵影',259928: '赵影',1240094: '赵影',368712: '赵影',924735: '赵影',799213: '赵影',552534: '赵影',519760: '赵影',947326: '赵影',261723: '赵影',947372: '赵影',254914: '赵影',56613: '赵影',297992 : '赵影',331526: '赵影',55490: '赵影',946495: '赵影',1240017: '赵影',150331: '赵影',175327: '赵影'}

lines = []

vips = []

tels = {}

relations = {}
root_relations = {}

source_file = csv.reader(file(source_file_name, 'rb'))
for the_line in source_file:
    lines.append(the_line)


def read():
    for line in lines:
        id = int(line[0])
        pid = int(line[1])
        tel = line[2]

        if id not in tels.keys():
            tels[id] = tel

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

f.writelines('guwenID, zxsID, phone, day, nickname \n')

for gonghuizhang in saler_guwens.keys():

    all_zxs = calculate(gonghuizhang)
    intersection = [v for v in all_zxs if v in vips]

    for vip_zxs in intersection:
        f.writelines(str(saler_guwens[gonghuizhang]) + ',' + str(vip_zxs) + ',' + tels[vip_zxs] + '\n')

f.close()

print 'done'

exit()




def sum_orders(list):
    a = 0
    for l in list:
        a += tels[l]
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
