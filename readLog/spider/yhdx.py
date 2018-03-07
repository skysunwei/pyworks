#-*- coding: UTF-8 -*-

import requests
from BeautifulSoup import BeautifulSoup


username = "whw"
password = "123456"

host_url = 'https://cp.youhaodongxi.com/admin/signin'
login_url = host_url + '/dosignin'
download_url = 'https://cp.youhaodongxi.com/admin/stat/index/orders'

para = {
    'email': username,
    'password': password,
}

headers = {
    'Host': 'cp.youhaodongxi.com',
    'Content-Length': '30',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://cp.youhaodongxi.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://cp.youhaodongxi.com/admin/signin/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2',
    'coockie' : 'adminid=139; adminname=whw; adminpassword=aea16d148dd9d7e33fc5875a6421ae48; token=66b03b468617d76b5fb959b0e4209a53; zg_did=%7B%22did%22%3A%20%2215fdb098fe1e0-01fcbc02427595-574e6e46-3d10d-15fdb098fe21c4%22%7D; _ga=GA1.2.880521568.1511208358; backpage=1; Hm_lvt_ea0e62011da521004044897d656fe734=1517473487; zg_19401c0971944c9d96d80f80ff64cddc=%7B%22sid%22%3A%201520389826063%2C%22updated%22%3A%201520389826994%2C%22info%22%3A%201520312580514%2C%22superProperty%22%3A%20%22%7B%5C%22Version%5C%22%3A%20%5C%225.2%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22wx.youhaodongxi.com%22%2C%22cuid%22%3A%20%22237%22%7D'
}


def read_storage_from_higo():
    session = requests.Session()

    # session.get(host_url)
    # session.post(login_url, para, headers=headers)

    result = session.get(download_url, headers=headers)

    print result.content

    soup = BeautifulSoup(result.text)
    table = soup.find("table")
    print table

read_storage_from_higo()