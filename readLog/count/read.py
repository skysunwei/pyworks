from collections import Counter

values = []

for line in open('data'):
    values.append(line.strip('\n'))

values_counts = Counter(values)

for key in values_counts.keys():
    print key, values_counts[key]

# top_2 = values_counts.most_common(2)
