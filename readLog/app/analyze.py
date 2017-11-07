# -*-coding:utf-8-*-

# SELECT saler.userid, saler.rank, saler.statustag FROM saler WHERE saler.status = 1

import csv
import xlrd
import pandas as pd

days = [20171103]


def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()


def read_xlsx(day, type):
    ids = []

    ios_file = '%s_%s_%s.xls' % (day, 'iOS', type)
    and_file = '%s_%s_%s.xls' % (day, 'Android', type)

    files = [ios_file, and_file]

    for file in files:

        workbook = xlrd.open_workbook(file)
        booksheet = workbook.sheet_by_name(workbook.sheet_names()[0])

        for row in range(booksheet.nrows):

            if row in [0]:
                continue

            value = booksheet.cell(row, 1).value

            if value is '':
                continue

            ids.append(int(value))

    return list(set(ids))


csvfile = file('saler.csv', 'rb')
reader = csv.reader(csvfile)

day = days[0]
active_ids = read_xlsx(day, 'Active')
action_ids = read_xlsx(day, 'Share') + read_xlsx(day, 'Retweet')

print '活跃人数 : ', len(active_ids)
print '有核心动作人数 :', len(action_ids)
print '甄选师人数 :', len(open("saler.csv").readlines())

saler_ids = []
saler_ranks = []
saler_tags = []
active_tags = []
action_tags = []

for line in reader:
    saler_id = int(line[0])

    saler_ids.append(saler_id)
    saler_ranks.append(line[1])
    saler_tags.append(line[2])

    active_tags.append('活跃' if saler_id in active_ids else '不活跃')
    action_tags.append('有' if saler_id in action_ids else '无')

df = pd.DataFrame({"id": saler_ids,
                   "rank": saler_ranks,
                   "tag": saler_tags,
                   "active": active_tags,
                   "action": action_tags
                   });

write_to_file = df.groupby(['active', 'action', 'rank']).size()

(write_to_file.to_frame()).to_csv(str(day) + '_rank.csv')

write_to_file = df.groupby(['active', 'action', 'tag']).size()

(write_to_file.to_frame()).to_csv(str(day) + '_tag.csv')
