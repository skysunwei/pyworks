# __author__ = 'colin'
#
# yhdx = []
#
# for line in open('yhdx'):
#     datas = line.strip('\n')
#     yhdx.append(datas)
#
# gei = {}
#
# for line in open('higo'):
#     datas = line.strip('\n').strip('\r').split(',')
#
#     try:
#         if datas[1] in yhdx:
#             haha = []
#             haha.append(datas[0])
#             haha.append(datas[2])
#
#             gei[datas[1]] = haha
#     except:
#         print
#
# # print gei
#
# for i in yhdx:
#     if i in gei.keys():
#         print i, ',', gei[i][0], ',', gei[i][1]
#     else:
#         print i

a = ['2017-05-22',
'2017-05-23',
'2017-05-24',
'2017-05-25',
'2017-05-26',
'2017-05-27',
'2017-05-28',
'2017-05-29',
'2017-05-30',
'2017-05-31',
'2017-06-01',
'2017-06-02',
'2017-06-03',
'2017-06-04',
'2017-06-05',
'2017-06-06',
'2017-06-07',
'2017-06-08',
'2017-06-09',
'2017-06-10',
'2017-06-11',
'2017-06-12',
'2017-06-13',
'2017-06-14',
'2017-06-15',
'2017-06-16',
'2017-06-17',
'2017-06-18',
'2017-06-19',
'2017-06-20',
'2017-06-21',
'2017-06-22']

for i in a:
    print "max(CASE orderday WHEN \'%s\' THEN num ELSE \'0\' END) AS \'%s\'," % (i, i)