import json

for line in open('usage'):

    data_string = json.loads(line)

    print int(data_string['money'])/100


