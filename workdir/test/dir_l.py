

import os
from datetime import datetime
# 利用os模块实现windows命令行中的’dir‘命令
# 输出文件的最后修改时间，文件类型，size ，name

pwd=os.path.abspath('.') #获取当前目录的绝对路径
print('%s的目录' % pwd)
print ('%s%10s%9s %s' % ('最后的修改时间','类型','size','文件名'))

for f in os.listdir(pwd):
    f_size = os.path.getsize(f) #文件大小
    modified_time=datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y%m%d %H:%M')
    f_type='<DIR>' if os.path.isdir(f) else '' #如果是子目录，类型是<DIR>
    print ('%s%9s%9d %s'% (modified_time,f_type,f_size,f))

filename=r'C:\users\zry71\PythonProjects\python笔记\IO_learn.py'
f_split=os.path.splitext(filename)
print(f_split) # ('C:\\users\\zry71\\PythonProjects\\python笔记\\IO_learn', '.py')
print('文件扩展名是：%s' % f_split[1]) # 文件扩展名是：.py
