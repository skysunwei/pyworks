higo = []

for line in open('higo'):
    higo.append(line.strip('\n'))

for line in open('yhdx'):
    if line.strip('\n') not in higo:
        print line

# controllers = {}

# for line in open('nav'):
#
#     data = line.strip('\n').split(',')
#     urls = data[1].split('/')
#     keyword = urls[-2]
#
#     if keyword not in controllers.keys():
#         controllers[keyword] = []
#     controllers[keyword].append(line)
#     # print data[0]
#     # print keyword
#
# for k in controllers:
#     print k
#     for i in controllers[k]:
#         print '     ' + i