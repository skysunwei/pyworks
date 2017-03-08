import time, datetime


def day_str_to_datetime(day_str):
    t = time.strptime(day_str, "%Y-%m-%d")
    return datetime.datetime(*t[:3])


def define_five(example):
    out = ''
    for i in range(0, len(example)-1):
        if example[i+1] - example[i] is not 1:
            out += ','
        else:
            out += '1'
    return out


for line in open('data'):
    datas = line.strip('\n').split('\t')

    userid = int(datas[0])

    days = datas[1].split(',')

    days.sort()

    first_day = day_str_to_datetime(days[0])

    day_intervals = []

    for day in days[1:]:
        current_day = day_str_to_datetime(day)
        day_intervals.append((current_day - first_day).days)

    one_day_intervals = define_five(day_intervals)

    for one_days in one_day_intervals.split(','):
        if len(one_days) > 4:
            print userid
            break


# example = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]




# definefive()