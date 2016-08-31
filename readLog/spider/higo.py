#-*- coding: UTF-8 -*-

import json
import requests

login_url = 'http://higo-express.cn/system/login.do'

username = "C00000083"
password = "yhdx_5ixc"

para = {
    'loginUserNO': username,
    'loginPassword': password,
}

url = 'http://higo-express.cn/wms/report/ajax/queryStockReport.do?warehouseID=1&ownerID=617'

headers = {
    'Host': 'higo-express.cn',
    'Content-Length': '55',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://higo-express.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': 'http://higo-express.cn/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2'
}

s = requests.Session()  # 可以在多次访问中保留cookie
s.get('http://higo-express.cn/')

result = s.post(login_url, data=json.dumps(para), headers=headers)  # POST帐号和密码，设置headers

print result

r = s.get(url)  # 已经是登录状态了

print r
