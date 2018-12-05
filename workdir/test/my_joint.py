#!/usr/bin/env python
# -*- coding:utf-8 -*-
def parse_allsite(allsite):
    if allsite.upper() == "TRUE":
        return True
    elif allsite.upper() == "FALSE":
        return False
    else:
        raise RuntimeError('allsite value is not False or True, please check it! ')

if __name__ == '__main__':

    a="false"
    b="world"
    c=".".join([a,b])
    istrue=parse_allsite(a)
    if istrue:
        print "True"
    else:
        print "False"
    print (c)