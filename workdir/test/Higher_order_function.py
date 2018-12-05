#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 高级函数，传递一个函数作为函数的参数
def add(a,b,f):
    return f(a)+f(b)
if __name__ == '__main__':
    print (add(5,-6,abs))
