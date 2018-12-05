#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Screen(object):
    # def __init__(self,width,height):
    #     self.__width=width
    #     self.__height=height

    @property
    def width(self):
        return  self.__width
    @width.setter
    def width(self,value):
        if not  isinstance(value,int):
            raise  ValueError('score must be an integer')
        if value < 0:
            raise ValueError('score must over zero')
        self.__width=value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0:
            raise ValueError('score must over zero')
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height

if __name__ == '__main__':
    # 测试:
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')