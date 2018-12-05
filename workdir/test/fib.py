#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def fib(max):
    n,a,b =0, 0, 1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return
if __name__ == '__main__':
    g=fib(6)
    for n in fib(6):
        print (n)
# while True:
#     try:
#         x=next(g)
#         print ('g:',x)
#     except StopIteration as e:
#         print ('Generator return value:', e.value)
#         break
#print fib(4)
# def fib(max):
#     n,a,b =0, 0, 1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n=n+1
#     return "done"
#
# print fib(4)