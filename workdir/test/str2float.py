#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456
from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1)+ reduce(fn,s2)/10.0**len(s2)
if __name__ == '__main__':
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')