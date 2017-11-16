# coding:utf-8

import csv

source_file_name = 'saler.csv'

lines = []
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
        order_num = int(line[2])

        if id not in payorders.keys():
            payorders[id] = order_num

        if pid not in relations.keys():
            relations[pid] = []
            relations[pid].append(id)
        else:
            relations[pid].append(id)


def root():
    ids = []
    pids = []

    for line in lines:
        id = int(line[0])
        pid = int(line[1])
        ids.append(id)
        pids.append(pid)

    rootsalers = [i for i in pids if i not in ids]
    rootsalers = list(set(rootsalers))
    rootsalers.sort()

    return rootsalers


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

print len(relations[237])
# print len(root_relations)


def calculate(k):
    if root_relations.has_key(k):
        i = 0
        # print k, len(relations[k]), relations[k]
        # print i

        for saler in root_relations[k]:
            i += calculate(saler)
            # print i

        return len(relations[k]) + i
    else:
        if k in relations:
            return len(relations[k])
        else:
            return 0


# print payorders


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

# print calculate(237)

# for k in root():
#     print k, ',', calculate(k), ',', count_orders(k)

f = file('output.csv', "w+")

for line in lines:
    userid = int(line[0])
    data = '%s,%s,%s\n' % (userid, calculate(userid), count_orders(userid))
    f.writelines(data)

for userid in root():
    data = '%s,%s,%s\n' % (userid, calculate(userid), count_orders(userid))
    f.writelines(data)

f.close()

print 'done'
