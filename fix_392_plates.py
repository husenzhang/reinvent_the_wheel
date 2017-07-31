#!/usr/bin/env python

import csv
from collections import defaultdict
import sys

"""reverse rows labels on a 392 plate
each A to P. Pseudocodes"""

def process(rows):
    labels, values = list(zip(*rows))
    rev_labels = reversed(labels)
    return list(zip(rev_labels, values))


if __name__ == '__main__':
    filin = sys.argv[1]
    fileout = sys.argv[2]
    with open(filin, 'rt') as fr:
        csr = csv.reader(fr)
        rows = [row for row in csr]
        start_with = {row[0][0] for row in rows} 
        dd = defaultdict(list)
        for row in rows:
            for sw in start_with:
                if row[0].startswith(sw):
                    dd[sw].append(row)
        new_rows = [process(dd[k]) for k in dd]
        new_rows = [row for sublist in new_rows for row in sublist] 
    with open(fileout, 'wt') as fw:
        csw = csv.writer(fw)
        csw.writerows(sorted(new_rows, key=lambda x: x[0]))
