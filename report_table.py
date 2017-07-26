#!/usr/bin/env python
"""parse .order file output a table
"""
import csv
from glob import glob

def main():
    header = ('ctg', 'len', 'cov', 'ori', 'cumlen')
    filepat = '*.order' 
    orders = glob(filepat)
    for order in orders: 
        sample = order[:2]
        fr = open(order, 'rt') 
        fw = open(order + '.csv', 'wt')
        csr = csv.reader(fr, delimiter='\t')
        csw = csv.writer(fw) 
        csw.writerow(header)

        cum_len = 0
        for line in csr:
            orient = line[1]
            node, node_n, length, length_n, cov, last = line[0].split('_')
            cov_n = last.split('.')[0]
            cum_len += int(length_n) 
            new_row = ['_'.join([node, node_n]), length_n, cov_n, orient, cum_len] 
            csw.writerow(new_row)
        fr.close()
        fw.close()

if __name__ == '__main__':
   main()
