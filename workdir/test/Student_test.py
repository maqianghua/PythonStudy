#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def get_grade(self):
        if self.score >100 or self.score<0:
            raise ValueError("the score in not valid")
        if self.score >=80 and self.score <=100:
            return 'A'
        elif self.score >=60 :
            return 'B'
        elif self.score >=0:
            return 'C'
