import csv
import sys

filepath = 'episodes/EC_0001/vo_script_table.csv'

with open(filepath, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

# Filter out empty rows
data = [r for r in data if len(r) >= 3 and r[0].strip()]

# Renumber VO_ID continuously
for i, row in enumerate(data):
    row[2] = str(i + 1)

with open(filepath, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print(f'Renumbered {len(data)} lines. Last VO_ID: {data[-1][2]}')
