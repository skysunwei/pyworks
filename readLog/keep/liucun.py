new_users = {}
for i in range(1, 8):
    new_users[i] = []

users = {}
for i in range(1, 8):
    users[i] = []

stay_users = {}
for i in range(1, 8):
    stay_users[i] = []

for line in open('months_bak'):
    datas = line.strip('\n').split(',')

    for i in range(1, len(datas)):
        if int(datas[i]) > 0:
            new_users[i].append(datas[0])
            break

for line in open('months_bak'):
    datas = line.strip('\n').split(',')

    for i in range(1, len(datas)):
        if int(datas[i]) > 0:
            users[i].append(datas[0])
            continue

for i in new_users.keys():
    for j in users.keys():
        if j >= i:
            stay = len(set(new_users[i]).intersection(set(users[j])))
            # print stay
            stay_users[i].append(stay)

headline = ''
for i in range(1, 8):
    headline += ',' + str(i) + 'yue'

print headline

for i in stay_users.keys():
    print str(i) + 'yue,' + str(stay_users[i])
