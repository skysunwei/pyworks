import csv
import random

csvfile = file('presentation-8-24.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    num = int(line[2])

    if num < 10:
        num = num * random.randint(20, 25)
    elif num < 50:
        num = num * random.randint(12, 14)
    elif num < 80:
        r = random.randint(5, 8)
        num = num * r
    else:
        num = num * random.randint(4, 5)

    num += random.randint(1, 9)
    # print line[2], num, num/int(line[2])
    print 'UPDATE `presentation` SET `popularity` = %s WHERE `presentation`.`presentationid` = %s;' % (num, line[0])