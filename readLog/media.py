import numpy

my_list = [1, 8, 9, 12, 3, 0, 1]

N = len(my_list)

narray = numpy.array(my_list)
sum1 = narray.sum()
narray2 = narray * narray
sum2 = narray2.sum()
mean = sum1/N
var = sum2/N - mean**2

print var


def avg(data):
    return sum(data) / len(data)


def median(data):
    data = sorted(data)
    size = len(data)

    if size % 2 == 0:
        return (data[size//2]+data[size//2-1])/2

    return data[(size-1)//2]

#
# print avg(my_list)
# print median(my_list)

