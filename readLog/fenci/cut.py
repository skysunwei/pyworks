#encoding=utf-8

import jieba
import jieba.posseg as pseg
import pandas as pd

from gensim import corpora, models

import re

jieba.load_userdict("ciku")

i = 0
cont = []

for line in open('share'):
    cont.append(line)

# 分词+选词
nwordall = []
for t in cont:
    words =pseg.cut(t)
    nword = ['']
    for w in words:
        if((w.flag == 'n'or w.flag == 'v' or w.flag == 'a') and len(w.word)>1):
            nword.append(w.word)
    nwordall.append(nword)

print nwordall

# # 3. 选择后的词生成字典
# dictionary = corpora.Dictionary(nwordall)

# #print dictionary.token2id
# # 生成语料库
# corpus = [dictionary.doc2bow(text) for text in nwordall]
# #tfidf加权
# tfidf = models.TfidfModel(corpus)
# # print tfidf.dfsx
# # print tfidf.idf
# corpus_tfidf = tfidf[corpus]
# # for doc in corpus_tfidf:
# #      print doc
#
# # 4. 主题模型lda，可用于降维
# #lda流式数据建模计算，每块10000条记录，提取50个主题
# lda = models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=50,     update_every=1, chunksize=10000, passes=1)
# for i in range(0,3):
#     print lda.print_topics(i)[0]
# #lda全部数据建模，提取100个主题
# #lda = models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=100, update_every=0, passes=20)
# #利用原模型预测新文本主题
# # doc_lda = lda[corpus_tfidf]