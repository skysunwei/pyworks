# weixin = []
# yhdx = []
# che = []
#
# count = 0
#
# for line in open('weixin'):
#     weixin.append(line)
#
# for line in open('che'):
#     che.append(line)
#     if line not in weixin:
#         print line
#
# for line in open('yhdx'):
#     yhdx.append(line)
#     if line not in weixin:
#         print line


zhongxin = []
yhdx = []

<<<<<<< HEAD
folder = '17-6'

for line in open(folder + '/a'):
    zhongxin.append(line.strip('\n'))

for line in open(folder + '/b'):
=======
folder = '17-11'

for line in open(folder + '/weixin.txt'):
    zhongxin.append(line.strip('\n'))

for line in open(folder + '/yhdx.txt'):
>>>>>>> 653c327b65b5cae9951d5c85e5fd420ca2714c94
    yhdx.append(line.strip('\n').split(',')[0])

print len(a)
print len(b)

a = {}
for i in zhongxin:
    a[i] = yhdx.count(i)

# print a

b = {}

for i in zhongxin:
    b[i] = zhongxin.count(i)

c = {}

for i in a:
    if i in b.keys() and a[i] != b[i]:
        c[i] = i

for i in c:
    print i, a[i], b[i]


print 'a duo'
print [i for i in zhongxin if i not in yhdx]

print
print 'b duo'
print [i for i in yhdx if i not in zhongxin]


# import csv
#
# csvfile = file('zhongxinmingxi.csv', 'rb')
# reader = csv.reader(csvfile)
#
# for i in reader:
#     print i
#     break


# print
#
# print [i for i in yhdx if i in weixin]

# weixin = []
# revoke = []
# compansate = []
# remove = []
#
# folder = '7-backup'
#
# for line in open(folder + '/weixin'):
#     weixin.append(line)
#
# for line in open(folder + '/compansate'):
#     compansate.append(line)
#
# for line in open(folder + '/revoke'):
#     revoke.append(line)
#
# for line in open(folder + '/remove'):
#     remove.append(line)
#     if line in revoke:
#         revoke.remove(line)
#     else:
#         print line, ': error'
#
# yhdx = revoke + compansate
#
# print [i for i in weixin if i not in yhdx]
#
# print
#
# print [i for i in yhdx if i not in weixin]
#
#
# print len(weixin)
# print len(yhdx)
#
# weixin.sort()
# yhdx.sort()
#
# for i in range(0, len(weixin) - 1):
#     if weixin[i] != yhdx[i]:
#         print weixin[i]
#         print weixin[i - 1]
#         print weixin[i + 1]
#         print i
#         break
