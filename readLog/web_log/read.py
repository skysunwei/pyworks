useraction = {}

domain_url = 'http://yhdx.5ixc.com/hao/'

first_page = '%s#!/share/explore' % domain_url
groupon_page = '%s#!/share/grouponStatus' % domain_url
groupon_page_from_timeline = '%s?from=timeline&isappinstalled=0#!/share/grouponStatus' % domain_url
groupon_page_from_groupmessage = '%s?from=groupmessage&isappinstalled=0#!/share/grouponStatus' % domain_url
coupon_page = '%s#!/share/receiveCoupon' % domain_url
merch_page = '%s#!/share/grouponMerch' % domain_url
merch_detail_page = '%s#!/share/merch' % domain_url
mine_order_page = '%s#!/share/mineOrder' % domain_url
order_detail_page = '%s#!/share/orderDetail' % domain_url
leader_apply_page = '%s#!/share/groupLeaderApply?userid=237' % domain_url



for line in open('route'):
    x = line.split('[')
    str_time = (x[1].split(']'))[0]
    data = (x[2].split(']'))[0].split(',"')
    userId = data[0].strip('"')
    url = data[1].strip('"')

    if str_time.find('2016-08-01') is 0:
        if userId not in useraction.keys():
            useraction[userId] = []

        useraction[userId].append({str_time: url})


def show_user_pages():
    for page in useraction['22']:
        print page.items()

useraction_without_saler = useraction


def remove_salers():
    print len(useraction_without_saler)

    for line in open('saler'):
        k = line.strip('\n')
        if k in useraction_without_saler.keys():
            useraction_without_saler.pop(k)

    print len(useraction_without_saler)


def user_page_view():
    groupon_page_users = []
    coupon_page_users = []
    first_page_users = []
    mine_order_page_users = []
    order_detail_page_users = []
    merch_detail_page_users = []
    leader_apply_page_users = []
    other_users = []

    for userId in useraction_without_saler.keys():
        page = useraction_without_saler[userId][0]
        page_url = page[page.keys()[0]]

        if page_url.find(groupon_page) is 0 or \
            page_url.find(groupon_page_from_timeline) is 0 or page_url.find(groupon_page_from_groupmessage) is 0:
            groupon_page_users.append(userId)
            continue

        if page_url.find(coupon_page) is 0:
            coupon_page_users.append(userId)
            continue

        if page_url.find(first_page) is 0:
            first_page_users.append(userId)
            continue

        if page_url.find(mine_order_page) is 0:
            mine_order_page_users.append(userId)
            continue

        if page_url.find(order_detail_page) is 0:
            order_detail_page_users.append(userId)
            continue

        if page_url.find(merch_detail_page) is 0:
            merch_detail_page_users.append(userId)
            continue

        if page_url.find(leader_apply_page) is 0:
            leader_apply_page_users.append(userId)
            continue

        other_users.append(userId)

    print 'groupon_page_users', ':', len(groupon_page_users)
    print 'coupon_page_users', ':', len(coupon_page_users)
    print 'first_page_users', ':', len(first_page_users)
    print 'mine_order_page_users', ':', len(mine_order_page_users)
    print 'order_detail_page_users', ':', len(order_detail_page_users)
    print 'merch_detail_page_users', ':', len(merch_detail_page_users)
    print 'leader_apply_page_users', ':', len(leader_apply_page_users)
    print 'other_user', ':', len(other_users)

    for userId in useraction_without_saler.keys():
        if userId in groupon_page_users:
            print userId
            for page in useraction_without_saler[userId]:
                print page


def show_pv_uv():
    uv = len(useraction)
    pv = 0
    groupon_page_pv = 0
    groupon_page_uv = 0
    view_groupon_page = 0

    merch_page_pv = 0
    merch_page_uv = 0
    view_merch_page = 0

    for userIds in useraction.keys():
        pv += len(useraction[userIds])
        for page in useraction[userIds]:
            # print sorted(a.items(), key=lambda d: d[0])
            for (k, v) in page.items():
                if v.find(groupon_page) >= 0:
                    groupon_page_pv += 1

                    if view_groupon_page is 0:
                        print '[', userIds, ']'
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


remove_salers()
user_page_view()