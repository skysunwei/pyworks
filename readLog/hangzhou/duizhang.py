import time
import datetime

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

today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterdaydatestr = today - oneday

infile = open('base.sql','r')
outfile = open('check.sql', 'w')

for line in infile:
    outfile.write(line.replace('todaysalerids', todaysalerids).replace('todaydatestr', yesterdaydatestr))

infile.close()
outfile.close()

print 'done'
