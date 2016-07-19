i = 1

for line in open('tuan'):
    tuan_list = line.split(' ')

    # print i

    for line in open('zhang'):
        tuan_zhang_list = line.split(' ')
        # print tuan_zhang_list[1]
        # print tuan_list[2]
        if tuan_zhang_list[1] == tuan_list[2]:
            # print tuan_list[0] + ', ' + tuan_zhang_list[0]
            print 'insert `temp-merchandise-saler-mapping`(`merchandiseid`, `userid`) values(' + tuan_list[0] + ', '+ tuan_zhang_list[0] + ');'

    i += 1