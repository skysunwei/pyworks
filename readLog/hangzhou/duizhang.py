import time

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

todaysalerids = ','.join(salerids)

todaydatestr = time.strftime('%Y-%m-%d', time.localtime(time.time()))

infile = open('base.sql','r')
outfile = open('check.sql', 'w')

for line in infile:
    outfile.write(line.replace('todaysalerids', todaysalerids).replace('todaydatestr', todaydatestr))

infile.close()
outfile.close()

print 'done'
