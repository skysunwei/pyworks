#encoding = utf-8

import jieba
import jieba.posseg as pseg
from collections import Counter

jieba.load_userdict("ciku")

cont = {}
for line in open('share'):
    datas = line.strip('\n').split(',')

    try:
        cont[int(datas[0])] = datas[1]
    except:
        continue

for t in cont.keys():
    words = pseg.cut(cont[t])

    cis = []

    for w in words:
        cis.append(w.word)

    lenth = len(cis)

    if lenth < 6:
        continue

    counter = Counter(cis)

    for k in counter.keys():
        if counter[k] > lenth/2:
            print t
            break