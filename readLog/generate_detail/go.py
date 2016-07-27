folder = 'import'

tabs = open(folder + 'tabs.html').read()

head = open(folder + 'head.html').read()
foot = open(folder + 'foot.html').read()

first = open(folder + '1.html').read()
second = open(folder + '2.html').read()
third = open(folder + '3.html').read()

rep = tabs.replace("diyige", first).replace("dierge", second).replace("disange", third)

result = head + rep + foot


f=file(folder + "result.html","w+")
f.writelines(result)
f.close()


