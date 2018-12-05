#coding:utf-8
"""
test pysam
"""
from sys import argv
#import pysam
#import numpy as np
#script, in_bam, to_file=argv

#bf = pysam.AlignmentFile(in_bam, "rb")
reads=[1,2,3,4,5,1,2,3,4]
#for r in bf:
#    reads.append(r.query_name)
reads_num=[]
for i in range(len(reads)):
    num=reads.count(reads[i])
    reads_num.append(reads[i])
    reads_num.append(num)
    reads_num.append("\n")
print reads_num
#out_file=open(to_file, 'w')
#out_file.write(reads_num)

print "Aright, all done."
#out_file.close()
#bf.close()
