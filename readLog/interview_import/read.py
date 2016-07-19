#-*- coding: UTF-8 -*-

import xlrd
import os
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

root_dir = "excel"


def is_useless_interview(feedback):
    if feedback is '':
        return True

    if '电话是否接通' in feedback:
        if '电话是否接通 : 是' in feedback:
            return False
        else:
            return True

    # print feedback
    return False

def str_to_timestamp(interview_time):
    try:
        time_array = time.strptime(interview_time, "%Y年%m月%d日%H:%M:%S")
        return int(time.mktime(time_array))
    except:
        return interview_time


def method_name():
    feed_back_collection = []

    for parent, dirNames, file_names in os.walk(root_dir):
        for file_name in file_names:

            excel_file = os.path.join(parent, file_name)

            data = xlrd.open_workbook(excel_file)
            sheet_names = data.sheet_names()

            for i in range(0, len(sheet_names)):

                table = data.sheets()[i]
                first_row_items = table.row_values(0)

                if '电话是否接通' in first_row_items:

                    if '回访时间' in first_row_items:
                        column_index_of_time = first_row_items.index('回访时间')
                    else:
                        print file_name + ', 没有找到回访时间.'
                        for row_item in first_row_items:
                            print row_item
                        continue

                    colume_str_of_tel = '联系电话'
                    if colume_str_of_tel in first_row_items:
                        column_index_of_tel = first_row_items.index(colume_str_of_tel)
                    else:
                        print file_name + ', 没有找到联系电话.'
                        for row_item in first_row_items:
                            print row_item
                        continue

                    for j in range(1, table.nrows):

                        interview_time = str(table.cell(j, column_index_of_time).value)
                        if interview_time is '':
                            continue

                        tel = str(table.cell(j, column_index_of_tel).value).strip('.0')

                        feed_back = ''
                        for k in range(column_index_of_time + 1, table.ncols):
                            feed_back_item = str(table.cell(j, k).value)
                            if feed_back_item.strip(' ') is not '':
                                feed_back += str(table.cell(0, k).value) + ' : ' + feed_back_item + '\n'

                        if is_useless_interview(feed_back):
                            continue

                        one_feedback = {}
                        one_feedback['tel'] = tel
                        one_feedback['time'] = str_to_timestamp(interview_time)
                        one_feedback['content'] = feed_back
                        feed_back_collection.append(one_feedback)

    return feed_back_collection

# str_to_timestamp()
feed_backs =  method_name()

for item in feed_backs:
    print "insert `customerservice`(`csnote`,`userid`,`startdateline`,`dateline`,`mobile`) values('%s',1,%s,%s,'%s'); "%(
        item['content'],\
        item['time'],\
        item['time'],\
        item['tel'])


# print is_useless_interview('电话是否接通 : 是')