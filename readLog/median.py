import numpy

my_list = \
    [7,18,2,2,11,4,8,13,1,3,23,4,6,1,28,6,8,5,1,1,44,30,6,46,7,2,72,1,2,3,5,29,6,1,8]

# N = len(my_list)
#
# narray = numpy.array(my_list)
# sum1 = narray.sum()
# narray2 = narray * narray
# sum2 = narray2.sum()
# mean = sum1/N
# var = sum2/N - mean**2
#
# print var


def avg(data):
    return sum(data) / len(data)


def median(data):
    data = sorted(data)
    size = len(data)

    if size % 2 == 0:
        return (data[size//2]+data[size//2-1])/2

    return data[(size-1)//2]

# print avg(my_list)
print median(my_list)

