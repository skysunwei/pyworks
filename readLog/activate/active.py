f = file('act.html', "w+")

for line in open('4-24_2'):
    data = line.strip('\n')
    strs = '<a href=\'https://cp.youhaodongxi.com/admin/sales/active/%s\'>%s</a>\n' % (data, data)
    f.writelines(strs)

f.close()
