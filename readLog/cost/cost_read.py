# -*-coding:utf-8-*-

import xlrd




def read_xlsx():

    workbook = xlrd.open_workbook('9.xlsx')
    f = file("update.sql", "w+")



    for sheet in workbook.sheet_names():
        booksheet = workbook.sheet_by_name(sheet)

        for row in range(booksheet.nrows):

            if row in [0]:
                continue

            suborderid = booksheet.cell(row, 0).value
            cost = booksheet.cell(row, 8).value
            store = booksheet.cell(row, 9).value

            sql = 'update `paysuborder` set `supplyprice` = %s, `repositoryfee` = %s where `suborderid` = %s;\n' % \
                (int(cost* 100) , int(store * 100), int(suborderid))

            f.writelines(sql)

    f.close()

read_xlsx()