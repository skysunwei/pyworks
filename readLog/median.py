import numpy

my_list = \
    [131,532,705,715,1041,274,2204,500,212,1445,685,533,135,724,366,492,472,95,58,542,782,120,484,773,772,224,428,265,21,134,264,149,126]

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

