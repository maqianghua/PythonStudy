#coding:utf-8
ln_path = 'last_name.txt'
fn_path = 'first_name.txt'
fn=[]
ln1=[]#单字名
ln2=[]#双字名

with open(fn_path, 'r') as f:
    for line in f.readlines():
        fn.append(line.split('\n')[0])#如果这里看不明白不妨试试对其中的一行使用split方法看看会返回回来什么结果
print(fn)
with open(ln_path, 'r') as f:
    for line in f.readlines():
        if len(line.split('\n')[0])==1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])
print (ln1)
print ('='*70)#分割线
print (ln2)