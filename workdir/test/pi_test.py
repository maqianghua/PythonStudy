#!/usr/bin/env python
# -*- coding:utf-8 -*-

import itertools
def pi(N):
    n=itertools.count(1,2) #去除奇数序列，从1开始，步长为2
    ns=itertools.takewhile(lambda x:x<=2*N,n) #取出前N个数
    num=list(ns) #将Iterator学历序列化
    sum=0
    for n in num:#循环，if判断取值
        if n%4==1:
            n=4/n
        else:
            n=-4/n
        sum += n
    return  sum

if __name__ == '__main__':
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
