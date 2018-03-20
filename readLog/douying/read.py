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

weixin_keys = []

for line in open('weixin', 'r'):
    weixin_keys.append(line.strip('\n'))

print weixin_keys

f = open('temp', 'r')
info = f.read()
f.close()

data = json.loads(info)

for show in data['members']:
    print show['sNickName'], show['sEmail'],

# videos = data['aweme_list']
# for video in videos:
    # signature = video['author']['signature']
    #
    # for key in weixin_keys:
    #     if key in signature:
    #         print key, ',,,,', signature
