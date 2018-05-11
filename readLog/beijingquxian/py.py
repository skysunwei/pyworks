import json

das = []

for line in open('data.txt'):
    da = json.loads(line.strip('\n'))

    das.append(da['end'])

print max(das)