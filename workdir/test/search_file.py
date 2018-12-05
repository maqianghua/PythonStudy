
# 在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，
# 并打印出相对路径
import os
# 中文文件夹会出错，未能解决
def search(path,s):
    listfile=[x for x in os.listdir(path) if os.path.isfile(os.path.join(path,x))]
    for f in listfile:
        # f 字符串包含s 字符串
        if s in f:
            print(os.path.join(path,f))
    listdir=[x for x in os.listdir(path) if os.path.isdir(os.path.join(path,x))]
    for d in listdir:
        search(os.path.join(path,d),s)

# if __name__ == '__main__':
search('../','c')
# import os
# def search_file(dir,sname):
#     # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。
#     # 它不包括 '.' 和'..' 即使它在文件夹中
#     if sname in os.path.split(dir)[1]:# 检查文件名里面是否包含sname
#         print (os.path.relpath(dir))#打印相对路径，相对指相对于当前路径
#     # Return True if path is an existing regular file.
#     # This follows symbolic links, so both islink() and isfile() can be true for the same path
#     if os.path.isfile(dir): #如果传入的dir直接是一个文件目录，他就没有子目录，就不用再遍历它的子目录了
#         return
#
#     for dire in os.listdir(dir): #遍历子目录，这里的dire为当前文件名
#         search_file(os.path.join(dir,dire),sname) #join 一下就变成了当前文件的绝对路径

