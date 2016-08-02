import time

useraction = {}


for line in open('route'):
    x = line.split('[')
    strtime = (x[1].split(']'))[0]
    data = (x[2].split(']'))[0].split(',"')

    userId = data[0].strip('"')
    url = data[1].strip('"')

    if strtime < '2016-07-29':
        # print strtime
        continue

    if strtime >= '2016-07-30':
        continue

    if userId not in useraction.keys():
        useraction[userId] = []

    useraction[userId].append({strtime: url})

# for page in useraction['28035']:
#     print sorted(page.items(), key=lambda d: d[0])

uv = 0
pv = 0
groupon_page_pv = 0
groupon_page_uv = 0
view_groupon_page = 0

merch_page_pv = 0
merch_page_uv = 0
view_merch_page = 0


first_page = 'http://yhdx.5ixc.com/hao/#!/share/explore'
groupon_page = 'http://yhdx.5ixc.com/hao/#!/share/grouponStatus'
merch_page = 'http://yhdx.5ixc.com/hao/#!/share/grouponMerch'



# for page in useraction['21']:
#     # print sorted(a.items(), key=lambda d: d[0])
#     print page.items()
#     for (k, v) in page.items():
#         if v == first_page:
#             first_page_pv += 1

uv = len(useraction)

# pv = 0

for userIds in useraction.keys():
    pv += len(useraction[userIds])
    for page in useraction[userIds]:
        # print sorted(a.items(), key=lambda d: d[0])
        for (k, v) in page.items():
            if v.find(groupon_page) >= 0:
                groupon_page_pv += 1

                if view_groupon_page is 0:
                    # print '[', userIds, ']'
                    view_groupon_page = 1
                    groupon_page_uv += 1

            if v.find(merch_page) >= 0:
                merch_page_pv += 1

                if view_merch_page is 0:
                    # print '[', userIds, ']'
                    view_merch_page = 1
                    merch_page_uv += 1

    view_groupon_page = 0
    view_merch_page = 0

print 'pv', pv
print 'groupon page pv', groupon_page_pv
print 'merch page pv', merch_page_pv

print

print 'uv', uv
print 'groupon page uv', groupon_page_uv
print 'merch page uv', merch_page_uv