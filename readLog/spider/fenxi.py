lines = []

for line in open('districts.txt'):
    lines.append(line)

datas = list(set(lines))

print len(datas)