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
        if w.flag != 'x':
            cis.append(w.word)

    lenth = len(cis)

    if lenth < 15:
        continue

    counter = Counter(cis)

    for k in counter.keys():

        if counter[k] > float(lenth)/5:
            print t, k, float(lenth)/5, lenth, counter[k], cont[t]
            break
