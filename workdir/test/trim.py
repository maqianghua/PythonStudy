#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 利用切片操作，实现一个trim()函数，
# 去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if s[:1] != " " and s[-1:] != " ":
        return s
    elif s[:1] == " ":
        return trim(s[1:])
    else :
        return trim(s[:-1])
print (trim("   hello    "))
print (trim("   hello"))
print (trim("hello    "))
print ("   hello    ")
