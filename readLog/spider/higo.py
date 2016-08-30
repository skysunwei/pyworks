#-*- coding: UTF-8 -*-

import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

#登录的主页面
hosturl = 'http://higo-express.cn/'

#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
loginBaiduUrl = 'http://higo-express.cn/system/login.do'

username = "C00000083"
password = "yhdx_5ixc"

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
resp = urllib2.urlopen(hosturl)
  
# second time do url request, the cookiejar will auto handle the cookie
para = {
    'loginUserNO': username,
    'loginPassword': password,
    }

postData = urllib.urlencode(para)
req = urllib2.Request(loginBaiduUrl, postData)
resp = urllib2.urlopen(req)
respInfo = resp.info()
