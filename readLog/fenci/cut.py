#encoding = utf-8

import jieba
import jieba.posseg as pseg

jieba.load_userdict("ciku")

cont = []
for line in open('share'):
    cont.append(line)

all_words = {}

for t in cont:
    words = pseg.cut(t)
    for w in words:
        if (w.flag == 'n' or w.flag == 'v' or w.flag == 'a') and len(w.word) > 1:
            if w.word not in all_words.keys():
                all_words[w.word] = []
            all_words[w.word].append(t)

revert_dict = sorted(all_words.iteritems(), key=lambda d: len(d[1]), reverse = True)

for (k, v) in revert_dict:
    if len(v) < 10:
        break

    print len(v), 'word: ', k
    for i in range(0, len(v)):
        print str(i+1) + ' : ' + v[i]