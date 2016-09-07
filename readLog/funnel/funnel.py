user_orders = {}

for line in open('source'):
    data = line.strip('\n').split(',')
    user_orders[int(data[0])] = int(data[1])

# print user_orders

all_user_num = 0
for k in user_orders:
    all_user_num += user_orders[k]
print 'all user num', all_user_num

lost_orders = {}
current_user_num = all_user_num
for k in user_orders:
    lost_orders[k] = str(round(float(user_orders[k]) * 100 / float(current_user_num), 2)) + '%'
    current_user_num = all_user_num - user_orders[k]
    print k, ',', lost_orders[k]
