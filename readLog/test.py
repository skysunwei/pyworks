import json

for line in open('usage.txt'):

    data_string = json.loads(line)

    print int(data_string['money'])/100


