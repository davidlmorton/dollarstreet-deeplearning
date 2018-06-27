import csv
import os
import sys


text_filenames = sys.argv[1:]

print(text_filenames)

images = []

for text_filename in text_filenames:
    with open(text_filename, 'r') as infile:
        lines = infile.readlines()

        for line in lines:
            if line.startswith('url'):
                url = 'https:' + line[5:-3]
            elif line.startswith('$'):
                value = int(line[1:])
            else:
                category = text_filename.split('.')[0]
                country = url.split('media/')[1].split('/image')[0]
                image_filename = url.split('/')[-1]
                images.append({
                    'category': category,
                    'country': country,
                    'filename': image_filename,
                    'url': url,
                    'value': value,
                })

with open('data.tsv', 'w', newline='') as csvfile:
    fieldnames = ['category', 'country', 'value', 'filename', 'url']
    writer = csv.DictWriter(csvfile, dialect=csv.excel_tab, fieldnames=fieldnames)

    writer.writeheader()
    for row in images:
        writer.writerow(row)
