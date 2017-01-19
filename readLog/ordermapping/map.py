line_one = ''
line_two = ''

i = 0
for line in open('zidingdan.txt'):

    datas = line.strip('\n').strip('\r')

    i += 1

    if i is 1:
        line_one = datas

    if i is 2:
        line_two = datas

line_one_data = []
line_two_data = []

for data in line_one.split(','):
    line_one_data.append(data)

for data in line_two.split(','):
    line_two_data.append(data)



for i in range(0, len(line_one_data) - 1):
    show = '\'%s\' AS \'%s\'' % (line_two_data[i], line_one_data[i])
    print show