#!/usr/bin/env python
# -*- coding:utf-8 -*-
from enum import Enum
class Gender(Enum):
    Male=0
    Female=1

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        # self.gender=gender
        self.gender=Gender(gender)


if __name__ == '__main__':
    bart = Student('Bart', Gender.Male)
    # print (bart.gender)
    # print (Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')
