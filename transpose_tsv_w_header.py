import csv

# the transposed file has an extra row 'taxonomy'

with open('otu_tax_relab.tsv', 'r') as infile,  \
	 open('otu_tax_L_otu.txt', 'w') as outfile:
	 reader = csv.reader(infile, delimiter = '\t')
	 next(reader, None)  # skip header, return None
	 transReader = zip(*reader) # unzip is same as transpose
	 csv.writer(outfile, delimiter = '\t').writerows(transReader)
