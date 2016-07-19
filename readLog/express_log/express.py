import json

for line in open('express.log'):
    try:
        item = json.loads(line)
        print item['lastResult']['data'][1]['context']
    except:
        print 'haha'

