higos ={}


for line in open('higo'):
    datas = line.strip('\n').strip('\r').split(',')

    try:
        info = []

        info.append(datas[0])
        info.append(datas[2])

        higos[datas[1]] = info
    except:
        continue

for line in open('yhdx.txt'):

    datas = line.strip('\n').strip('\r')

    try:
        print datas,',', higos[datas][0],',', higos[datas][1]
    except:
        print ''

