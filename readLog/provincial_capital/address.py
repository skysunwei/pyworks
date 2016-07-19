#-*- coding: UTF-8 -*-

input = '地址是北京市朝阳区太阳宫二街1号院太阳公元二期3号楼1602'

sheng = ['江苏省']

zhiXiaShi = {1: '北京市', 2: '天津市', 3: '上海市', 4: '重庆市'}


for (key, shi) in zhiXiaShi.items():
    print shi[:-3]
    if input.find(shi) > 0 or input.find(shi[:-3]) > 0:
        print str(key) + ', ok'

        # 找到这个市下面的区;

qu = ''

