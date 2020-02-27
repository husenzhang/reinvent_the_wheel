import csv

# read tsv to dict ,parse dict field when read
# sort ('target', 'size')

parserTuples = [('query',  None),
                 ('target', None),
                 ('id',     float),
                 ('alnlen', int),
                 ('mism',   int),
                 ('opens',  int),
                 ('qlo',    int),
                 ('qhi',    int),
                 ('tlo',    int),
                 ('thi',    int),
                 ('evalue', float),
                 ('qseq',   None)]

parsers = {a:b for a, b in parserTuples}

fields = [a for a, _ in parserTuples]

def parse_item(field, value, parsers):
    """ field, value are strings, parsers is a dict.
        helper function for parse_dict"""
    parser = parsers.get(field)
    return value if parser is None else parser(value)

def parse_dict(input_dict, parsers):
    """ a dict has many items, return a dict"""
    return { field : parse_item(field, value, parsers)
             for field, value in input_dict.items() }

def query_size(query):
    """ helper function to deal with size annotation"""
    size = int(query.strip(';').split('=')[-1])
    return size

def qseq_to_exon(row):
    start, end = row['qlo'], row['qhi']
    return row['qseq'][start:end]

def sort_then_topn(data, field1, field2, topn):
    return data.sort(key=lambda x: (x[field1], x[field2]))[:topn]

def tsv_dict(tsv, fdnames, parsers):
    """parse occurs for each row, which is a dict"""
    with open(tsv, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t', fieldnames = fdnames)
        data = []
        for row in reader:
            row = parse_dict(row, parsers)
            row['size'] = query_size(row['query'])
            row['qseq'] = qseq_to_exon(row)        
            data.append(row)
    return data

def write_fasta(df, fasta_name, seed_label= False):
    """usage: write_fasta(df, 'out/derep.fa', seed_label = True) """
    with open(fasta_name, 'w') as f:
        for _, row in df.iterrows():
            if not seed_label:
                header = '>' + row['qid']
            else:
                header = '>' + row['qid'] + row['target']
            f.write(header + '\n' + row['qseq'] + '\n')

def main(filename):
<<<<<<< HEAD
    """return None; write csv and fasta one per line """
    csv_name, fa_name = filename + '.csv',  filename + '.fa'

    write_fasta(df, fa_name, seed_label = True)

=======
    """ """
>>>>>>> 3a2f4e4d1b8139ea545a2b4cf5d2035cb26e5343
