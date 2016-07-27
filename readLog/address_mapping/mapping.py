#-*- coding: UTF-8 -*-

rule = {}
source = {}

for t in range(41, 51):
    rule[t] = []

# print rule


for line in open('district'):
    districts = line.strip('\n').split(',')

    kv = {}
    kv[districts[2]] = districts[0]
    # print kv
    rule[int(districts[1])].append(kv)

# for i in range(41, 51):
#     print len(rule[i])
#     for j in range(len(rule[i])):
#         print rule[i][j]

for line in open('source'):
    sources = line.strip('\n').split(',')

    key = int(sources[1])
    # print key

    if key in rule.keys():
        # print key
        for j in range(len(rule[key])):
            # print rule[key][j]
            # print sources[3]

            try:
                if sources[3] in rule[key][j].keys():
                    print 'update `recipientaddress` set `district`=', \
                        rule[key][j][sources[3]] ,' where `addressid`=', sources[0],';'
                    # break
                # else:
                    # print line
                    # print 'not in'
            except Exception,e:
                # print line
                # print Exception, ':', e
                break
