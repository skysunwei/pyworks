salerids = []

for line in open('salerid'):
    try:
        datas = line.strip(')\n').split('(', -1)

        salerid = ''
        for data in datas:
            if ',' in data:
                salerid = data.split(',')[1].strip(' ')

        salerids.append(salerid)

    except Exception, e:
        print line, e

print ','.join(salerids)
