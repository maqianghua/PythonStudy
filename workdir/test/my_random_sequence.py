#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

alphabet = 'ACGT'

# 随机定义序列长度
size = random.randrange(16,21)
print (size)
seq=[]
for _ in range(size):
    # 获得序列，存入数组
    # print (_)
    seq.append(alphabet[random.randrange(0,4)])

seq = ''.join(seq) + 'GG'
print  (seq)