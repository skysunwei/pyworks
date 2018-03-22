#!/usr/bin/env python

#coding:utf-8

import requests
import json
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# url = ''
#
# page = requests.get('https://www.douyin.com/aweme/v1/hot_aweme/?cursor=0&count=36&aweme_id=6532791544951344392')
#
# if page.status_code == 200:
#
#     # beijing_districts = json.loads(page.text)
#
#     print page.text

"uid": "73325533060",
"avatar_larger": {
"url_list": [
"https://p1.pstatp.com/aweme/1080x1080/5fd7000aa51205a26528.jpeg",
"https://pb3.pstatp.com/aweme/1080x1080/5fd7000aa51205a26528.jpeg",
"https://pb3.pstatp.com/aweme/1080x1080/5fd7000aa51205a26528.jpeg"
],
"uri": "5fd7000aa51205a26528"
},
"birthday": "1988-07-10",
"nickname": "回忆圈",
"short_id": "106196286",
"gender": 1,
"avatar_medium": {
"url_list": [
"https://p1.pstatp.com/aweme/720x720/5fd7000aa51205a26528.jpeg",
"https://pb3.pstatp.com/aweme/720x720/5fd7000aa51205a26528.jpeg",
"https://pb3.pstatp.com/aweme/720x720/5fd7000aa51205a26528.jpeg"
],
"uri": "5fd7000aa51205a26528"
},
"signature": "",
"avatar_thumb": {
"url_list": [
"https://p1.pstatp.com/aweme/100x100/5fd7000aa51205a26528.jpeg",
"https://pb3.pstatp.com/aweme/100x100/5fd7000aa51205a26528.jpeg",
"https://pb3.pstatp.com/aweme/100x100/5fd7000aa51205a26528.jpeg"
],
"uri": "5fd7000aa51205a26528"
},
"is_verified": true,
"unique_id": ""

class Author(object):
    signature = 0
    uid = ''
    gender = ''

    def __init__(self, merchandiseId, merchandiseName, merchandiseTag, name, price, qimai):
        self.merchandiseId = merchandiseId
        self.merchandiseName = merchandiseName
        self.merchandiseTag = merchandiseTag
        self.name = name

        if qimai is 0:
            self.money = price
        else:
            self.money = price * qimai

    pass

weixin_keys = []

for line in open('weixin', 'r'):
    weixin_keys.append(line.strip('\n'))

print weixin_keys

f = open('temp', 'r')
info = f.read()
f.close()

data = json.loads(info)

videos = data['aweme_list']
for video in videos:
    signature = video['author']['signature']
    signature = video['author']['signature']

    for key in weixin_keys:
        if key in signature:
            print key, ',,,,', signature
