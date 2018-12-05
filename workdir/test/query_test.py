#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Query(object):
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print ('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s ...'% self.name)

if __name__ == '__main__':
    with Query('bob') as q:
        q.query()