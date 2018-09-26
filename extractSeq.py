# -*- coding: utf-8 -*-
#!/usr/bin/python

genome = open('hgTables.txt', 'r')
genes = open('geneName.txt', 'r')
seqList = genome.readlines()
geneList = genes.readlines()
print(len(seqList))

for i in seqList:
    for gene in geneList:
        if i == gene:
            seqFiles = open('/home/leia/code/' + gene, 'wa')
            seqFiles.write(i)
            p = seqList.index(i)
            while (seqList[p+1][0] != '>'):
                seqFiles.write(seqList[p+1])
                p = p+1
            seqFiles.close()
    genes.close()
  #i = p
genome.close()
