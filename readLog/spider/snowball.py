#-*- coding: UTF-8 -*-

import requests
from BeautifulSoup import BeautifulSoup


username = "skysunwei@gmail.com"
password = "20010911"

host_url = 'http://yhdx.5ixc.com/admin/signin'
login_url = host_url + '/dosignin'
download_url = 'http://yhdx.5ixc.com/admin/merchandise/statistical/notdeliverorder'

para = {
    'email': username,
    'password': password,
}

headers = {
    'Host': 'yhdx.5ixc.com',
    'Content-Length': '30',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://yhdx.5ixc.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://yhdx.5ixc.com/admin/signin/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2'
}


def read_storage_from_higo():
    session = requests.Session()

    session.get(host_url)
    session.post(login_url, para, headers=headers)
    result = session.get(download_url)

    # print result.content

    soup = BeautifulSoup(result.text)
    table = soup.find("table")
    print table

read_storage_from_higo()