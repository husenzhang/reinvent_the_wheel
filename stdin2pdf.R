#!/usr/bin/env Rscript

library('ggplot2')
theme_set(theme_bw())
library(reshape2)


d = read.delim(file("stdin"), header=F)

print(length(names(d)))
if (length(names(d) == 3))  { 
   d = melt(d, id.vars = names(d)[1])
   p = ggplot(d, aes(factor(d[,1], levels= d[order(d$value),][,1]), value,fill=variable)) + 
          geom_bar(stat = 'identity', position='dodge') +
          theme(legend.position=c(0.8,0.2))+
          guides(fill=guide_legend(title=NULL)) + 
          xlab(NULL) +
          ylab(NULL) +
          coord_flip()

} else {
p = ggplot(d, aes(factor(d[,1], levels= rev(d[,1])), d[,2])) + 
          geom_bar(stat = 'identity') +
          xlab(NULL) +
          ylab(NULL) +
          coord_flip()
}
ggsave('plot.pdf', plot=p, height=5, width=5)
