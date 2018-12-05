#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 假设我们用一组tuple表示学生名字和成绩
# 请用sorted()对上述列表分别按名字排序
L=[('Bob',75), ('Adam',92), ('Bart',66),('Lisa',88)]
def by_name(t):
    return t[0].lower()
def by_name_2(t):
    return t[0]
def by_score(t):
    return t[1]
if __name__ == '__main__':
    L2=sorted(L,key=by_name, reverse=True)
    print (L2)
    L1 = sorted(L, key=by_name_2, reverse=True)
    print (L1)
    L3=sorted(L,key=by_score,reverse=True)
    print (L3)