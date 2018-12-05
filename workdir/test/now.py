#!/usr/bin/env python
# -*- coding:utf-8 -*-
def log(func):
    def wrapper(*args, **kw):
        print ('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print ('2018-7-9')

if __name__ == '__main__':
        print (now())