#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 错位相加
def triangles():
    L=[1]
    while True:
        yield L
        L=[sum(i) for i in zip([0]+L ,L+[0])]
if __name__ == '__main__':
    g=triangles()
    for n in range(12):
        print (next(g))

