#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b=1,1
            for x in range(item):
                return a
        if isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L

if __name__ == '__main__':
    f=Fib()
    print (f[0:5])
    print (f[:10])
