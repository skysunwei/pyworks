# coding:utf-8

base = {}

for line in open('cover_out'):
    datas = line.strip('\n').split(',')
    base[datas[0]] = int(datas[1])

# print base

money = 0
trunk_line_fee = 3
local_express_fee = 6
shunfeng_express_fee = 17

count = 0

for line in open('expressfee'):
    datas = line.strip('\n').split(',')

    pay_fee = int(datas[2])
    buy_quantity = int(datas[3])
    #
    if datas[5] == '顺丰快递':
        money += pay_fee + (trunk_line_fee + local_express_fee - shunfeng_express_fee) * buy_quantity
        count += buy_quantity
        # print money
        # break
    else:
        try:
            money += (pay_fee + buy_quantity * local_express_fee - base[datas[1]])
        except:
            print datas[1]
            continue

    # print money

    # break

print money
print count