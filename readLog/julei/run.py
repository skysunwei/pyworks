order_ids = {}
time_ids = {}

times = []
orders = []


def median(my_list):
    data = sorted(my_list)
    size = len(data)

    if size % 2 == 0:
        return (data[size//2]+data[size//2-1])/2
    return data[(size-1)//2]

for line in open('ids'):

    datas = line.strip('\n').split(',')

    id = int(datas[0])
    order = int(datas[1])
    time = int(datas[2])

    orders.append(order)
    times.append(time)

    if time_ids.has_key(time) is False:
        time_ids[time] = []
    time_ids[time].append(id)

    if order_ids.has_key(order) is False:
        order_ids[order] = []
    order_ids[order].append(id)


md_order = median(orders)
md_time = median(times)

print md_order, md_time

zx = []
zs = []
yx = []
ys = []

for time in time_ids.keys():
    for order in order_ids.keys():
        if time <= md_time and order <= md_order:
            zx += [val for val in time_ids[time] if val in order_ids[order]]
        if time <= md_time and order > md_order:
            zs += [val for val in time_ids[time] if val in order_ids[order]]
        if time > md_time and order <= md_order:
            yx += [val for val in time_ids[time] if val in order_ids[order]]
        if time > md_time and order > md_order:
            ys += [val for val in time_ids[time] if val in order_ids[order]]

file_names = {'zx': zx, 'zs' : zs, 'ys' : ys, 'yx' : yx}

for file_name in file_names.keys():
    distrit_file = '%s.txt' % (file_name)
    f = file(file_name, "w+")
    for data in file_names[file_name]:
        f.writelines(str(data) + '\n')
    f.close()

print 'zx : ', len(zx)
print 'zs : ', len(zs)
print 'yx : ', len(yx)
print 'ys : ', len(ys)