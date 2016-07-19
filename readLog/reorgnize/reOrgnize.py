shenShiDict = {}
shiGroup = []

for line in open('keyifa.txt'):
    xingZheng = line.split(',')

    shen = int(xingZheng[0])
    shi = xingZheng[1].strip('\n')

    if shen in shenShiDict:
        shenShiDict[shen].append(shi)
    else:
        shiGroup = [shi]
        shenShiDict[shen] = shiGroup

keys = shenShiDict.keys()
keys.sort()
for key in keys:
    print '\'' + str(key) + '\' => ' + str(shenShiDict[key]) + ','
