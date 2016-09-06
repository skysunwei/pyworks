def avg(data):
    return sum(data) / len(data)


def median():
    my_list = []

    for line in open('median/source'):
        my_list.append(int(line.strip('\n')))

    data = sorted(my_list)
    size = len(data)

    if size % 2 == 0:
        return (data[size//2]+data[size//2-1])/2

    return data[(size-1)//2]

# print avg(my_list)
print median()

