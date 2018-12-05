#coding:utf-8

class TestA:
    attr=1
obj_a=TestA()

TestA.attr=42
print (obj_a.attr)