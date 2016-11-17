# coding:utf-8


import turtle


source_file_name = 'source.txt'


nicknames = {}
relations = {}
root_relations = {}


def read():

    for line in open(source_file_name):
        line_data = line.split(',')
        id = int(line_data[0])
        pid = int(line_data[1])
        nickname = line_data[2]

        if pid not in nicknames.keys():
            nicknames[pid] = nickname

        if pid not in relations.keys():
            relations[pid] = []
            relations[pid].append(id)
        else:
            relations[pid].append(id)


def root():
    ids = []
    pids = []

    for line in open(source_file_name):
        line_data = line.split(',')
        id = int(line_data[0])
        pid = int(line_data[1])
        ids.append(id)
        pids.append(pid)

    rootsalers = [i for i in pids if i not in ids]
    rootsalers = list(set(rootsalers))
    rootsalers.sort()

    return rootsalers


def size():

    # print rootsalers

    for line in open(source_file_name):
        line_data = line.split(',')
        id = int(line_data[0])
        pid = int(line_data[1])

        if id in relations.keys() and pid in relations.keys():
            if pid not in root_relations.keys():
                root_relations[pid] = []
                root_relations[pid].append(id)
            else:
                root_relations[pid].append(id)

read()
root()
size()

print relations
print root_relations


def calculate(k):
    if root_relations.has_key(k):
        i = 0
        # print k, len(relations[k]), relations[k]
        # print i
        for saler in root_relations[k]:
            i = i + calculate(saler)
            # print i
        return len(relations[k]) + i
    else:
        if k in relations:
            return len(relations[k])
        else:
            return 0

# print calculate(50112)

for k in root():
    print k, ',', calculate(k)

