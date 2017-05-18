library(phyloseq)
library(ggplot2)
theme_set(theme_bw())
library(DESeq2)
library(pheatmap)

pheat <- function(ps, L){              # L: int 1-7; 1:OTU
  RankNum <- paste0('Rank', L)
  if (L > 1)
    {ps <- tax_glom(ps, taxrank = RankNum)}
  dds.data <- phyloseq_to_deseq2(ps, ~ Strain) # here ----------
  dds = DESeq(dds.data)
  res = results(dds)
  alpha = 0.05                                 # here --------- 
  sigtab = res[which(res$padj < alpha), ]
  sigtab = cbind(as(sigtab, "data.frame"), 
                 as(tax_table(ps)[rownames(sigtab), ], "matrix"))
  log2.norm.counts <- assay(normTransform(dds))[rownames(sigtab), ]
  rownames(log2.norm.counts) <- sigtab[ ,RankNum]
  
  df <- as.data.frame(colData(dds)[ , c('Strain')]) # here -------
  rownames(df) <- colnames(log2.norm.counts)
  colnames(df) <- 'MouseStrain'                    # here --------
  
  pdf( paste0(RankNum, '.pdf') )
  p = pheatmap(log2.norm.counts, annotation_col = df)
  dev.off()
  write.csv(log2.norm.counts, file = paste0(RankNum, '.csv'),
            quote = F, row.names = F)
}

ps <- import_biom("out/json")
for (L in 1:7) {
  pheat(ps, L)
}
