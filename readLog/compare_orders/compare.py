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


weixin = []
yhdx = []

folder = '10-backup'

for line in open(folder + '/weixin-jiaoyi'):

    weixin.append(line.strip('\n'))

for line in open(folder + '/yhdx-jiaoyi'):
    yhdx.append(line.strip('\n'))

print [i for i in weixin if i not in yhdx]

print

print [i for i in yhdx if i not in weixin]

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
