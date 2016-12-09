moneys = []

now = 39.9

for line in open('source'):
    money = line.strip('\n').split(',')[1]

    try:
        moneys.append(float(money))
    except:
        print money

i = 0
for money in moneys:
    i += 1
    if now > money:
        break

size = len(moneys)

print i
print size
print float((size - i)) * 100 / size, '%'



