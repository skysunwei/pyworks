# -*-coding:utf-8-*-

import xlrd
from BeautifulSoup import BeautifulSoup

def read_xlsx():
    workbook = xlrd.open_workbook('video.xlsx')
    first_sheet = workbook.sheet_names()[0]
    booksheet = workbook.sheet_by_name(first_sheet)

    p = []

    for row in range(booksheet.nrows):

        if row in [0, 1]:
            continue

        id = booksheet.cell(row, 0).value
        title = booksheet.cell(row, 1).value
        html = booksheet.cell(row, 2).value

        soup = BeautifulSoup(html).find('video')

        info = '<p>' \
               '<a href="http://yhdx.5ixc.com/hao/#!/share/merch?id=%s">%s</a>' \
               '</p>' % (int(id), title)

        if soup is not None:
            p.append(info)
            p.append(soup)

    return p




template = open('template.html').read()
print template
for l in read_xlsx():
    print l

print '</body></html>'

