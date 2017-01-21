import csv
from operator import itemgetter

def csv_data(csvname):
    """Usage: df  =  csv_data('b6.tsv')"""
    data = []
    with open(csvname, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            data.append(line)
    return data

def size_sort(data):
    """add size in the last column then sort by k1, k12"""
    for row in data:
        size = int(row[0].strip(';').split('=')[-1])
        row.append(size)
    data.sort(key=itemgetter(1, 12), reverse=True)
    return data

def delete_pattern(df, pattern):
    """if pattern exists in a row, delete that row"""
    [ df.pop(i) for i, row in enumerate(df) if pattern in row]
    return df
