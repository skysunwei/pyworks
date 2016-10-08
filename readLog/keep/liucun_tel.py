# coding: utf-8

import csv


def read_data(file_name):
    source_file_data = []

    csv_file = file(file_name, 'rb')
    reader = csv.reader(csv_file)

    for line in reader:
        source_file_data.append(line)

    csv_file.close()

    del source_file_data[0]

    return source_file_data


current_month = 9
next_month = current_month + 1

