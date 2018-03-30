# coding:utf-8

import csv

source_file_name = 'saler.csv'

#saler_guwens = {27997: 69, 38617: 70, 67413: 71, 145007: 72, 48416: 73, 89159: 74, 237: 75, 81560: 76}

# saler_guwens = {27997: '星星', 38617: '王哲君', 67413: '笑笑', 145007: '小颖', 48416: '靖', 89159: '建新', 237: '赵影', 81560: '峥'}

saler_guwens = {237: '赵影', 67413: '笑笑', 1167969: '白夜', 832631: '赵影',1199916: '赵影',671652: '赵影',1196675: '赵影',205591: '赵影',249008: '赵影',116331: '赵影',172146: '赵影',662782: '赵影',315755: '赵影',453944: '赵影',614297: '赵影',182797: '赵影',1229910: '赵影',448600: '赵影',903071: '赵影',223835: '赵影',837491: '赵影',884846: '赵影',820274: '赵影',4331: '赵影',840989: '赵影',1190862: '赵影',1189790: '赵影',1210048: '赵影',1116989: '赵影',208583: '赵影',1183059: '赵影',654652: '赵影',925336: '赵影',259928: '赵影',1240094: '赵影',368712: '赵影',924735: '赵影',799213: '赵影',552534: '赵影',519760: '赵影',947326: '赵影',261723: '赵影',947372: '赵影',254914: '赵影',56613: '赵影',297992 : '赵影',331526: '赵影',55490: '赵影',946495: '赵影',1240017: '赵影',150331: '赵影',175327: '赵影',
                29512: '赵影',887388: '赵影',717667: '赵影',136915: '赵影',944214: '赵影',33280: '赵影',694550: '赵影',1061250: '赵影',381742: '赵影',880768: '赵影',198905: '赵影',1108890: '赵影',1110344: '赵影',303949: '赵影',1239642: '赵影',252395: '赵影',977958: '赵影',1085206: '赵影',860188: '赵影',407058: '赵影',617423: '赵影',607489: '赵影',1238272: '赵影',1243367: '赵影',959625: '赵影',998107: '赵影',455158: '赵影',234461: '赵影',136513: '赵影',263801: '赵影',244494: '赵影',635484: '赵影',325542: '赵影',1245087: '赵影',1057041: '赵影',369956: '赵影',898240: '赵影',531369: '赵影',1245240: '赵影',248579: '赵影',954229: '赵影',483984: '赵影',1083148: '赵影',311377: '赵影',1219274: '赵影',447324: '赵影',122704: '赵影',358185: '赵影',1227476: '赵影',617325: '赵影',791418: '赵影',208774: '赵影',1195415: '赵影',743130: '赵影',202249: '赵影',1026413: '赵影',363896: '赵影',1126084: '赵影',1121384: '赵影',820243: '赵影',1109419: '赵影',1208486: '赵影',545781: '赵影',356510: '赵影',79801: '赵影',62722: '赵影',1239250: '赵影',1178175: '赵影',899494: '赵影',1235548: '赵影',625148: '赵影',973646: '赵影',257200: '赵影',566111: '赵影',125485: '赵影',1189762: '赵影',663190: '赵影',1226866: '赵影',603156: '赵影',615666: '赵影',551131: '赵影',1228862: '赵影',242669: '赵影',1241883: '赵影',1244015: '赵影',1051217: '赵影',1165634: '赵影',845314: '赵影',1129474: '赵影',425030: '赵影',188528: '赵影',1243641: '赵影',242403: '赵影',4964: '赵影',1065781: '赵影',968750: '赵影',1156178: '赵影',1155012: '赵影',94898: '赵影',636380: '赵影',4286: '赵影',370769: '赵影',238652: '赵影',337559: '赵影',1190448: '赵影',774794: '赵影',1199583: '赵影',6724: '赵影',1176773: '赵影',11038: '赵影',1200102: '赵影',290805: '赵影',1243509: '赵影',1233611: '赵影',340988: '赵影',503806: '赵影',151452: '赵影',90546: '赵影',31691: '赵影',1198171: '赵影',240991: '赵影',180403: '赵影',186778: '赵影',17102: '赵影',890664: '赵影',1141618: '赵影',23910: '赵影',1226765: '赵影',1092752: '赵影',1226951: '赵影',463575: '赵影',296614: '赵影',50447: '赵影',215378: '赵影',975929: '赵影',1186313: '赵影',363284: '赵影',893092: '赵影',1225323: '赵影',1163777: '赵影',1242813: '赵影',48769: '赵影',150973: '赵影',480461: '赵影',539381: '赵影',578649: '赵影',972699: '赵影',915320: '赵影',53526: '赵影',1141690: '赵影'}

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
