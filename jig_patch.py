
from Bio import SeqIO

helper = '09_contigs_pseudo.fa'
genome = '08_contigs_pseudo.fa' 
gf   = SeqIO.read(genome, 'fasta').seq
hlpr = SeqIO.read(helper, 'fasta').seq

n_len = 100
pads = 'N' * n_len
chunk = 30
n_show = 100
fill_show_len = 200

seq_flank = []
start = 0
while start < len(gf) - n_len:
    n_left = gf.find(pads, start = start)
    n_right= n_left + n_len
    left, right = n_left-chunk, n_right+chunk
    stride = n_right - start
    start += stride
    seq_flank.append(gf[left:right])

for seq in seq_flank:
    lf, rt = seq[:chunk], seq[-chunk:]
    st = hlpr.find(lf)
    ed = hlpr.find(rt, start=st)
    if (st != -1) and (ed != -1):
        ed = ed + chunk
        fill = hlpr[st:ed]
        if len(fill) > fill_show_len:
           fill_show = fill[:fill_show_len]
        else:
           fill_show = fill
        print(genome[:2], seq[:chunk+n_len]+ seq[-chunk:])
        print(helper[:2], fill_show, '-'*10)
        n_pads = fill.count(pads)
        print('  ', st, ed, ed-st, n_pads)
