import csv

reader_6 = csv.reader(file('6.csv', 'rb'))
reader_7 = csv.reader(file('7.csv', 'rb'))

for line in reader_6:
    print line