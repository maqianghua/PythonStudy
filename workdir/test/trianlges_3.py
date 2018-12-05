#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
def triangles():
    L=[1]
    while True:
        yield L
        L=[sum(i) for i in zip([0]+L ,L+[0])]
def main():
    n=0
    results=[]
    for x in triangles():
        print (x)
        results.append(x)
        n=n+1
        if n==10:
            break
    if results == [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1],
        [1,5,10,10,5,1],
        [1,6,15,20,15,6,1],
        [1,7,21,35,35,21,7,1],
        [1,8,28,56,70,56,28,8,1],
        [1,9,36,84,126,126,84,36,9,1]
    ]:
        print ("测试成功！")
    else:
        print ("测试失败")
    for y in results:
        print (y)
main()