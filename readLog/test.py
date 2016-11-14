# coding:utf-8

from numpy import *


def loadData():#coding:utf-8

from numpy import *

def loadData():
    return [[1,1,1,0,0],
             [2,2,2,0,0],
             [3,3,3,0,0],
             [5,5,3,2,2],
             [0,0,0,3,3],
             [0,0,0,6,6]]

data=loadData()

u,sigma,vt=linalg.svd(data)

print sigma

sig3=mat([[sigma[0],0,0],
      [0,sigma[1],0],
      [0,0,sigma[2]]])

print u[:,:3]*sig3*vt[:3,:]
    return [1, 1, 1, 0, 0]


data = loadData()

u, sigma, vt = linalg.svd(data)

print sigma

sig3 = mat([[sigma[0], 0, 0],
            [0, sigma[1], 0],
            [0, 0, sigma[2]]])

print u[:, :3] * sig3 * vt[:3, :]



# higo = []
#
# for line in open('higo'):
#     higo.append(line.strip('\n'))
#
# for line in open('yhdx'):
#     if line.strip('\n') not in higo:
#         print line

# controllers = {}

# for line in open('nav'):
#
#     data = line.strip('\n').split(',')
#     urls = data[1].split('/')
#     keyword = urls[-2]
#
#     if keyword not in controllers.keys():
#         controllers[keyword] = []
#     controllers[keyword].append(line)
#     # print data[0]
#     # print keyword
#
# for k in controllers:
#     print k
#     for i in controllers[k]:
#         print '     ' + i
