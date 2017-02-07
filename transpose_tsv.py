#!/usr/bin/env python
""" transpose a tsv file from stdin 
remove the header and write to stdout
"""

import csv
import sys

# the transposed file has an extra row 'taxonomy'

infile = sys.stdin
outfile = sys.stdout

reader = csv.reader(infile, delimiter = '\t')
next(reader, None)  # skip header, return None
transReader = zip(*reader) # unzip is same as transpose
csv.writer(outfile, delimiter = '\t').writerows(transReader)
