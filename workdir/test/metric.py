#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time, functools
def exeTime(func):
    def newFunc(*args,**args2):
        t0=time.time()
        # print "@%s,{%s} start" % (time.strftime("%X",time.localtime()),func.__name__)
        back=func(*args, **args2)
        # print "@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__)
        print "@%.3fs token for {%s}" % (time.time()-t0, func.__name__)
        return back
    return newFunc
@exeTime
def foo():
    for i in xrange(10000000):
        pass
if __name__ == '__main__':
    foo()
# def metric(fn):
#     print ('%s execute in %s ms' % (fn.__name__, 10.24))
#     return  fn
#
# if __name__ == '__main__':
#     # 测试
#     @metric
#     def fast(x, y):
#         time.sleep(0.0012)
#         return x + y;
#
#
#     @metric
#     def slow(x, y, z):
#         time.sleep(0.1234)
#         return x * y * z;
#
#
#     f = fast(11, 22)
#     print (f)
#     s = slow(11, 22, 33)
#     print (s)
#     if f != 33:
#         print('测试失败!')
#     elif s != 7986:
#         print('测试失败!')