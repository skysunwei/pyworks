# coding: utf-8

userViews = {}

def read_month_log_file(log_file):
    for line in open(log_file):

        try:
            x = line.split('[')
            str_time = (x[1].split(']'))[0]

            data = (x[2].split(']'))[0].split(',"')

            userId = data[0].strip('"')
            client = data[2].strip('"')
            url = data[1].strip('"')

            if userId not in userViews.keys():
                userViews[userId] = 1

            # print userId, client, url, str_time

        except:
            print line
            break

    print len(userViews)

read_month_log_file('all10.log')

