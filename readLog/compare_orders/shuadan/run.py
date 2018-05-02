#-*- coding: UTF-8 -*-

import xlrd
import sys

reload(sys)
sys.setdefaultencoding('utf8')

all_ids = {}
fa_ids = {}

workbook = xlrd.open_workbook('20180425.xlsx')
booksheet1 = workbook.sheet_by_name(workbook.sheet_names()[0])
booksheet2 = workbook.sheet_by_name(workbook.sheet_names()[3])

for row in range(booksheet1.nrows):

    if row in [0]:
        continue

    id = int(booksheet1.cell(row, 0).value)
    nickname = booksheet1.cell(row, 1).value
    phone = booksheet1.cell(row, 2).value

    all_ids[id] = '%s, %s' % (str(phone).strip('.0'), nickname)

for row in range(booksheet2.nrows):

    if row in [0]:
        continue

    id = int(booksheet1.cell(row, 0).value)
    nickname = booksheet1.cell(row, 1).value
    phone = booksheet1.cell(row, 2).value

    fa_ids[id] = '%s, %s' % (str(phone).strip('.0'), nickname)


no_ids = list(set(all_ids.keys()).difference(set(fa_ids.keys())))

print len(no_ids)

f = file('out.csv', "w+")

f.write('手机号, #var1#')

for id in no_ids:
    strs = '%s\n' % (all_ids[id])
    f.write(strs)

f.close()

print 'done'
