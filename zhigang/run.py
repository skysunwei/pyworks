__author__ = 'colin'

yhdx = []

for line in open('yhdx'):
    datas = line.strip('\n')
    yhdx.append(datas)

gei = {}

for line in open('higo'):
    datas = line.strip('\n').strip('\r').split(',')

    try:
        if datas[1] in yhdx:
            haha = []
            haha.append(datas[0])
            haha.append(datas[2])

            gei[datas[1]] = haha
    except:
        print

# print gei

for i in yhdx:
    if i in gei.keys():
        print i, ',', gei[i][0], ',', gei[i][1]
    else:
        print i