#!/usr/bin/env python
# -*- coding:utf-8 -*-
from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Sep','Oct','Nov','Dec'))

for name, member in Month.__members__.items():
    print (name,'=>',member, ',', member.value)

@unique #Unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
for name, member in Weekday.__members__.items():
    # print (name,'=>',member)
    print(name, '=>', member, ',', member.value)