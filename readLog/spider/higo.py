import json
import requests

host_url = 'http://higo-express.cn/'
login_url = host_url + 'system/login.do'
download_url = host_url + 'wms/report/ajax/queryStockReport.do?warehouseID=1&ownerID=617'

username = "C00000083"
password = "yhdx_5ixc"

para = {
    'loginUserNO': username,
    'loginPassword': password,
}

headers = {
    'Host': 'higo-express.cn',
    'Content-Length': '55',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://higo-express.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': host_url,
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2'
}

s = requests.Session()
s.get(host_url)
s.post(login_url, data=json.dumps(para), headers=headers)
r = s.get(download_url)

r.encoding='utf-8'

print r.encoding
print r.content

# print stores.encode(r.encoding).decode('utf-8')
