# coding: utf-8

user_actions = {}

domain_url = 'http://yhdx.5ixc.com/hao/'

first_page = '%s#!/share/explore' % domain_url
leader_page = 'groupLeader'
groupon_page = 'grouponStatus'
groupon_page_from_timeline = '%s?from=timeline&isappinstalled=0#!/share/grouponStatus' % domain_url
groupon_page_from_groupmessage = '%s?from=groupmessage&isappinstalled=0#!/share/grouponStatus' % domain_url
coupon_page = '%s#!/share/receiveCoupon' % domain_url
merch_page = '%s#!/share/grouponMerch' % domain_url
merch_detail_page = '%s#!/share/merch' % domain_url
mine_order_page = '%s#!/share/mineOrder' % domain_url
order_detail_page = '%s#!/share/orderDetail' % domain_url
leader_apply_page = '%s#!/share/groupLeaderApply?userid=237' % domain_url
discover_page = '%s#!/share/discover' % domain_url


groupon_page_users = []
leader_page_users = []
coupon_page_users = []
first_page_users = []
mine_order_page_users = []
order_detail_page_users = []
merch_detail_page_users = []
leader_apply_page_users = []
discover_page_users = []
other_users = []


def read_log(log):
    result = {}

    if log.find('a:', 0) == 0:
        details = log.split(':', 2)
        detail_datas = details[2].strip('{').strip('}').split(';')

        for i in range(0, int(details[1])):
            result[read_log(detail_datas[i * 2])] = read_log(detail_datas[i * 2 + 1])

        return result

    if log.find('i:', 0) == 0:
        return int(log.split(':')[1])

    if log.find('s:', 0) == 0:
        return log.split(':')[2].strip('"')


def read_log_file(log_file, day):
    for line in open(log_file):

        try:
            datas = line.strip('\n').split(']')
            str_time = str(datas[0].strip('['))
            temp_datas = datas[1].split(' ', 4)
            userId = temp_datas[3]
            detail_datas = eval(temp_datas[4].split(' {')[0])
            url = detail_datas['1']
            client = detail_datas['2']

            # print datas

            # print line.strip('\n').split(' ', 5)[5]
            #
            # print read_log(line.strip('\n').split(' ', 4)[4])
            #
            # break

            if str_time.find(day) is 0:
                if userId not in user_actions.keys():
                    user_actions[userId] = []

                user_actions[userId].append({str_time: url})

                sql = 'INSERT INTO view(userId, url, client, dateline, day) ' \
                      'VALUES(%s, \'%s\', \'%s\', \'%s\', \'%s\');' \
                      % (userId, url, client, str_time, day)

        except Exception, e:
            print Exception, ":", e
            print line
            break


def show_user_pages(user_id):
    for page in user_actions[user_id]:
        print page.items()


user_actions_without_saler = user_actions


def remove_salers():
    print 'all user num', len(user_actions_without_saler)

    for line in open('saler'):
        k = line.strip('\n')
        if k in user_actions_without_saler.keys():
            user_actions_without_saler.pop(k)

    print 'user without saler num', len(user_actions_without_saler)
    print


def user_first_page_view():

    for userId in user_actions_without_saler.keys():
        fist_page_view = user_actions_without_saler[userId][0]
        page_url = fist_page_view[fist_page_view.keys()[0]]

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

        if page_url.find(leader_page) is 0:
            leader_page_users.append(userId)
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

        if page_url.find(discover_page) is 0:
            discover_page_users.append(userId)
            continue

        other_users.append(userId)

    print 'groupon_page_users', ':', len(groupon_page_users)
    print 'leader_page_users', ':', len(leader_page_users)
    print 'coupon_page_users', ':', len(coupon_page_users)
    print 'first_page_users', ':', len(first_page_users)
    print 'mine_order_page_users', ':', len(mine_order_page_users)
    print 'order_detail_page_users', ':', len(order_detail_page_users)
    print 'merch_detail_page_users', ':', len(merch_detail_page_users)
    print 'leader_apply_page_users', ':', len(leader_apply_page_users)
    print 'discover_page_users', ':', len(discover_page_users)
    print 'other_user', ':', len(other_users)

    # for userId in user_actions_without_saler.keys():
    #     if userId in groupon_page_users:
    #         print userId
    #         for fist_page_view in user_actions_without_saler[userId]:
    #             print fist_page_view


def user_next_page_count(current_page_users, next_page):
    print 'all', len(current_page_users)

    count_num = 0

    for user_id in current_page_users:
        for page in user_actions[user_id]:
            for page_url in page.values():
                if page_url.find(next_page) >= 0:
                    count_num += 1
                    break

    print 'then view', count_num


def show_pv_uv(search_page, page_name):
    uv = len(user_actions)
    pv = 0
    page_pv = 0
    page_uv = 0
    view_page = 0

    for userIds in user_actions.keys():
        pv += len(user_actions[userIds])
        for page in user_actions[userIds]:

            # print sorted(a.items(), key=lambda d: d[0])
            for (k, v) in page.items():
                if v.find(search_page) >= 0:
                    page_pv += 1

                    if view_page is 0:
                        # print '[', userIds, ']'
                        view_page = 1
                        page_uv += 1

        view_page = 0

    print 'pv', pv
    print 'uv', uv
    print

    print page_name, 'pv', page_pv
    print page_name, 'uv', page_uv
    print

read_log_file('20170413.log', '2017-04-13')

# print len(user_actions)

show_pv_uv(first_page, 'firstpage')
show_pv_uv(discover_page, 'discoverpage')
show_pv_uv(groupon_page, 'grouponpage')
show_pv_uv(leader_page, 'leaderpage')

# remove_salers()
#
# show_pv_uv(discover_page, 'discoverpage')
#
#
# user_first_page_view()
# user_next_page_count(groupon_page_users, leader_page)
# user_next_page_count(groupon_page_users, merch_page)
# user_next_page_count(discover_page_users, merch_detail_page)

# print first_page_users
