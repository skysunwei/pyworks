# coding: utf-8

import csv

file_source = 'buyer'
output_file_name = file_source + '_liucun.csv'

current_month = 7
next_month = current_month + 1

new_users = {}
for i in range(1, next_month):
    new_users[i] = []

users = {}
for i in range(1, next_month):
    users[i] = []

stay_users = {}
for i in range(1, next_month):
    stay_users[i] = []


for line in open(file_source):
    line_data = line.strip('\n').split(',')

    for i in range(1, len(line_data)):
        if int(line_data[i]) > 0:
            new_users[i].append(line_data[0])
            break

for line in open(file_source):
    line_data = line.strip('\n').split(',')

    for i in range(1, len(line_data)):
        if int(line_data[i]) > 0:
            users[i].append(line_data[0])
            continue

for i in new_users.keys():
    for j in users.keys():
        if j >= i:
            stay = len(set(new_users[i]).intersection(set(users[j])))
            # print stay
            stay_users[i].append(stay)


headline = ['月份']
for i in range(1, next_month):
    headline.append(str(i) + '月')

# print headline

output_file = file(output_file_name, 'wb')
writer = csv.writer(output_file)
writer.writerow(headline)

data = []

for i in stay_users.keys():
    data.append([str(i) + '月'] + ['']*(current_month - len(stay_users[i])) + stay_users[i])
    # print str(i) + '月,' + str(stay_users[i])

# print data

writer.writerows(data)

output_file.close()
