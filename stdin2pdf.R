#!/usr/bin/env Rscript

library(ggplot2)

d = read.delim(file("stdin"), header=F)
print(names(d))

if ( length(names(d)) == 2 ) {
p = ggplot(d, aes(V1, V2)) + 
          geom_bar(stat = 'identity') +
          theme_bw() +
          coord_flip()
} else {
p = ggplot(d, aes(V1)) + geom_histogram()
}  

ggsave('plot.pdf', plot=p, width=5, height=5)
