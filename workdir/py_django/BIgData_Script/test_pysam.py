#coding:utf-8
"""
test pysam
"""
import pysam
import numpy as np
def test0():
    import pysam
    bf = pysam.AlignmentFile("in.bam", "rb")
    for pileupcolumn in bf.pileup("chrM", 300, 301):
        for read in [a1 for a1 in pileupcolumn.pileups if a1.alignment.mapq>30]:
            if not read.is_del and not read.is_refskip:
                if pileupcolumn.pos + 1 == 301:
                    print read.alignment.query_name, read.alignment.query_sequence[read.query_position]
    bf.close()
if __name__ == '__main__':
    test0()