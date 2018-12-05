#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import re
import os
import sys
patt=re.compile(r'(?P<hour>\d{1,2})\:(?P<minute>\d{1,2})\:(?P<second>\d{1,2})')
# from datetime import datetime
s=['4:5:28','0:5:8','0:20:29']
# str_time_1=time.strptime(str[1],"%H:%M:%S")
# str_time_2=time.strptime(str[0],"%H:%M:%S")
# print (str_time_1+str_time_2)
def strtime2second(s):
    try:
        d=patt.match(s).groupdict()
        return int(d['hour'])*3600+int(d['minute'])*60+int(d['second'])
    except:
        pass

def seconds2time(s):
    hour=s//3600
    minutes=s%(3600)//60
    second=s%60
    total_hour=s/3600.0
    # return str(hour):str(minutes):str(second)
    return (('%d:%d:%d\t%0.2f')% (hour,minutes,second,total_hour))

if __name__ == '__main__':
    # 测试1
    print(strtime2second(s[1]))
    print(seconds2time(strtime2second(s[1])))
    # 运行2
    # total=[]
    # with open('%s' % sys.argv[1],'r') as f:
    #     for line in f.readlines():
    #         line_temp=line[2:]
    #         temp_total_seconds=0
    #         for s in line_temp:
    #             temp_total_seconds=temp_total_seconds+strtime2second(s)
    #         total.append(seconds2time(temp_total_seconds))
    # with open('%s' % sys.argv[1],'r') as f:
    #     all_line=f.readlines()
    # with open('%s' % sys.argv[2],'w') as fw:
    #     for i in range(len(total)):
    #         fw.write('%s\t%s\n' % (all_line[i].strip('\n'), total[i]))

    # 测试3
    # print(strtime2second(s[0])-strtime2second(s[1]))
    # print(seconds2time(strtime2second(s[0])+strtime2second(s[1])))
    # print (s[1:])
    # 测试4
    # str_time=time.strptime(s[1],"%H:%M:%S")
    # print (str_time)