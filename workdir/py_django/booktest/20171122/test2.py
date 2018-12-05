#coding:utf-8

NASDAQ_code = {'BIDU':'Baidu', 'SINA':'Sina'}
print NASDAQ_code

a_set = {1,2,3,4}
a_set.add(5)#添加
a_set.discard(5)#删除
print a_set
num_list =[6,2,7,4,1,3,5]
print(sorted(num_list))
sorted (num_list, reverse=True)
print(sorted (num_list, reverse=True))
print num_list
# for a,b in zip(num, str):
#     print (b, 'is', a)