import json

controllers = {}

for line in open('nav'):

    data = line.strip('\n').split(',')
    urls = data[1].split('/')
    keyword = urls[-2]

    if keyword not in controllers.keys():
        controllers[keyword] = []
    controllers[keyword].append(line)

    # print data[0]
    # print keyword

for k in controllers:
    print k
    for i in controllers[k]:
        print '     ' + i


