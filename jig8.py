import glob
import subprocess

refgnm = '08_contigs_pseudo.fa'
ref_prefix = refgnm.split('_')[0] 
py2 = '/usr/local/bin/python'
lastdot = '/data/MicrobiomeCore/Linuxbrew/bin/last-dotplot'

samples = glob.glob('*.fasta')

for sample in samples:
    sname = sample.split('_')[0]
    makedb = 'lastdb -cR01 %s %s' %(ref_prefix, refgnm) 
    promer = 'promer -p %s %s %s' %(sname, refgnm, sample)
    tiling = 'show-tiling %s.delta > %s.tiling' %(sname, sname  )
    makenn = 'createTilingPseudoMolecule %s.tiling %s' %(sname, sample)
    lastal = 'lastal %s %s_contigs_pseudo.fa > %s_pseudo.msf' %(ref_prefix, sname, sname)
    pltpng = '%s %s %s_pseudo.msf %s.png' %(py2, lastdot, sname, sname)
    
    script = '\n'.join([makedb, promer, tiling, makenn, lastal, pltpng ])
    print('*'*10)
    print(script)
    subprocess.call(script, shell=True)


