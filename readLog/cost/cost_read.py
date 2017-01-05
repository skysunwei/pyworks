# -*-coding:utf-8-*-

import xlrd


def read_xlsx():

    month = '12'
    file_name = '%s.xlsx' % month
    sql_file = "%s_update.sql" % month

    workbook = xlrd.open_workbook(file_name)
    f = file(sql_file, "w+")

    for sheet in workbook.sheet_names():
        booksheet = workbook.sheet_by_name(sheet)

        for row in range(booksheet.nrows):

            if row in [0]:
                continue

            subOrderid = booksheet.cell(row, 0).value
            cost = booksheet.cell(row, 8).value
            store = booksheet.cell(row, 9).value

            try:
                sql = 'update `paysuborder` set `supplyprice` = %s, ' \
                      '`repositoryfee` = %s ' \
                      'where `suborderid` = %s;\n' % \
                    (int(cost * 100), int(store * 100), int(subOrderid))
            except:
                continue

            f.writelines(sql)

    f.close()

    print 'done'

read_xlsx()