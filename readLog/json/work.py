__author__ = 'colin'

import json

outs = []

for line in open('data'):
    # print line

    obs = json.loads(line)
    for ob in obs:
        outs.append(ob["goods"]["name"])

outs = list(set(outs))

for out in outs:
    print out
