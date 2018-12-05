#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 函数的返回结果不是返回值，而是函数
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return  ax
    return sum
if __name__ == '__main__':
    f=lazy_sum(1,3,5,7,9)
    print f #<function sum at 0x05AA7930>
    print f() #25