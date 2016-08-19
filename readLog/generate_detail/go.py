#-*- coding: UTF-8 -*-

folder = 'jinguo/'

tabs = open(folder + 'tabs.html').read()

head = open(folder + '开头.txt').read()
foot = open(folder + '结尾.txt').read()

first = open(folder + '绿奇异果.txt').read()
second = open(folder + '金奇异果.txt').read()
# third = open(folder + '3.txt').read()

rep = tabs.replace("diyige", first).replace("dierge", second)

result = head + rep + foot


f=file(folder + "result.txt", "w+")
f.writelines(result)
f.close()


