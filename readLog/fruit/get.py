#-*- coding: UTF-8 -*-

wujin = 0
bajin = 0

for line in open('pinlei'):
    kv = line.split(',')
    if kv[0] == '5斤装':
        wujin += int(kv[1])
    if kv[0] == '8斤装':
        bajin += int(kv[1])

print wujin
print bajin