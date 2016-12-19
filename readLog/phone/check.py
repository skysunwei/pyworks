#coding=utf-8

import re
import sys
import os

p2 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')

for line in open('phones'):

    datas = line.strip('\n').split(',')

    phonematch = p2.match(datas[3])

    if phonematch:
        continue
    else:
        print line