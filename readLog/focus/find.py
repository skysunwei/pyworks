search = []
all = []


for line in open('all'):
    all.append(line.strip('\n').split(',')[0])

for line in open('search'):
    search.append(line.strip('\n'))


# a = [i for i in all if i not in search]
#
# print len(a)
#
# b = [i for i in search if i not in all]
#
# print len(b)


print len(list(set(all).intersection(set(search))))