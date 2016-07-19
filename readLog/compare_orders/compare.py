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

for line in open('weixin'):
    weixin.append(line)

for line in open('yhdx'):
    yhdx.append(line)
    if line not in weixin:
        print line

print len(weixin)
print len(yhdx)