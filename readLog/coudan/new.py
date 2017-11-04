import itertools

list1 = [1, 2, 3]
list2 = []
list3 = []

for i in range(1, len(list1)+1):
    iter = itertools.combinations(list1, i)
    list2.append(list(iter))

print(list2)


for items in list2:
    for item in items:
        list3.append(sum(item))

print(list3)
