#-*- coding: UTF-8 -*-

import csv
import time
import json
import requests
from urllib import unquote

username = "sunwei"
password = "colinsun"

host_url = 'http://yhdx.5ixc.com/'
login_url = host_url + 'admin/signin/dosignin'
download_url = host_url + 'admin/merchandise/statistical/notdeliverorder'

para = {
    'email': username,
    'password': password,
}

headers = {
    'Host': 'higo-express.cn',
    'Content-Length': '30',
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

    data = result.text.encode(result.encoding).decode(result.encoding)
    print data


read_storage_from_higo()