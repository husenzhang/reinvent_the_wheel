library('ggplot2')

d = read.delim(file("stdin"), header=F)
print(names(d))
p = ggplot(d, aes(V1, V2)) + 
          geom_bar(stat = 'identity') +
          theme_bw() +
          coord_flip()

ggsave('plot.pdf', plot=p)
