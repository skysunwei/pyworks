infos = []
womens = []

#----------



for line in open('data'):
    datas = line.strip('\n').split('\t')
    infos.append(datas[1])

infos = list(set(infos))



print len(infos)

#----------

for line in open('women'):
    datas = line.strip('\n').split('|')

    try:
        womens.append(datas[2])
    except:
        continue

womens = list(set(womens))

print len(womens)

#----------

inster = list(set(womens).intersection(set(infos)))

print len(inster)
print inster