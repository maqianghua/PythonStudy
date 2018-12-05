#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def triangles():
    L=[1]
    while True:
        # 你的第一种算法，只需要把 yield L改成L[:len(L)] 我觉得是python的list内部的list和元组差不多
        # 都存在引用不变的情况 因为list 里面的list内存地址可能一直没变
        yield L[:len(L)]
        # yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
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