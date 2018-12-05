#coding:utf-8
from sys import argv
from os.path import exists
import os
import pysam
import numpy as np
from pysam import VariantFile
script, bam_file, vcf_file, output_bam_file=argv

bamfile=pysam.AlignmentFile(bam_file, "rb")
vcffile=VariantFile(vcf_file)
output_bamfile=pysam.AlignmentFile(output_bam_file,"wb", template=bamfile)
for rec in vcffile.fetch():
    for read in bamfile.fetch():
        if (rec.pos==read.pos):
            output_bamfile.write(read)

output_bamfile.close()
bamfile.close()
vcffile.close()


