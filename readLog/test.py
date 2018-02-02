# -*-coding:utf-8-*-

# SELECT saler.userid, saler.rank, saler.statustag FROM saler WHERE saler.status = 1

import csv
import xlrd
import pandas as pd

workbook = xlrd.open_workbook('a.xlsx')

booksheet = workbook.sheet_by_name(workbook.sheet_names()[0])

merchandise_names = []
merchandise_categories = []
merchandise_is_news = []
merchandise_salers = []

saler_new_merchandises = {}
saler_old_merchandises = {}

for row in range(booksheet.nrows):

    merchandise = booksheet.cell(row, 0).value.strip('\n')
    merchandise_names.append(merchandise)

    category = booksheet.cell(row, 1).value.strip('\n')
    merchandise_categories.append(category)

    is_new = booksheet.cell(row, 2).value.strip('\n')
    merchandise_is_news.append(is_new)

    saler = booksheet.cell(row, 3).value.strip('\n')
    merchandise_salers.append(saler)

    # print is_new
    if is_new == u'新品':
        if saler_new_merchandises.has_key(saler):
            saler_new_merchandises[saler].append(merchandise)
        else:
            saler_new_merchandises[saler] = [merchandise]
    else:
        if saler_old_merchandises.has_key(saler):
            saler_old_merchandises[saler].append(merchandise)
        else:
            saler_old_merchandises[saler] = [merchandise]

merchandise_salers = list(set(merchandise_salers))

for saler in merchandise_salers:
    len_new = 0
    if saler_new_merchandises.has_key(saler):
        len_new = len(saler_new_merchandises[saler])

    len_old = 0
    if saler_old_merchandises.has_key(saler):
        len_old = len(saler_old_merchandises[saler])

    print saler,',',len_new,',', len_old



