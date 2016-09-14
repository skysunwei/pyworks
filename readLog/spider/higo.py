#-*- coding: UTF-8 -*-

import csv
import time
import json
import requests
from urllib import unquote


username = "C00000083"
password = "yhdx_5ixc"

table_name = '`op-sunwei-higo`'

host_url = 'http://higo-express.cn'
login_url = host_url + '/system/login.do'
download_url = host_url + '/wms/report/ajax/queryStockReport.do?warehouseID=1&ownerID=617'

para = {
    'loginUserNO': username,
    'loginPassword': password,
}

headers = {
    'Host': 'higo-express.cn',
    'Content-Length': '55',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': host_url,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': host_url,
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2'
}


def read_storage_from_higo():
    session = requests.Session()
    session.get(host_url)
    session.post(login_url, data=json.dumps(para), headers=headers)
    result = session.get(download_url)

    print result.encoding

    file_name = unquote(result.headers['Content-Disposition'].split('=')[1])
    data = result.text.encode(result.encoding).decode(result.encoding)

    csv_file = file(file_name, "w+")
    csv_file.write(data.encode('utf-8'))
    csv_file.close()

    return file_name


def higo_storage_analyse(file_name):

    print 'truncate table %s;' %table_name

    reader = csv.reader(file(file_name, 'rb'))

    fist_line = True

    for line in reader:

        if fist_line is True:
            fist_line += False
            continue

        product_code = line[0].strip('yhdx')
        product_name = line[1]

        # time
        import_time_read = line[2]

        if len(import_time_read) > 8:
            import_time_read = import_time_read[:-1]

        import_time = ''
        try:
            import_time = time.strftime("%Y-%m-%d", time.strptime(import_time_read, "%Y%m%d"))
        except:
            try:
                import_time = time.strftime("%Y-%m-%d", time.strptime(import_time_read, "%Y-%m-%d"))
            except:
                print 'time format error!'

        import_num = line[3]
        real_num = line[4]
        danwei = line[5]

        print 'insert %s(`code`,`name`,`time`,`num`,`real`, `danwei`) ' \
              'values(%s,\'%s\',\'%s\',%s,%s,\'%s\');' % \
              (table_name, product_code, product_name, import_time, import_num, real_num, danwei)


higo_storage_analyse(read_storage_from_higo())