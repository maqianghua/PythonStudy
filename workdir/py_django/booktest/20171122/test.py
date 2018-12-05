import time
a=[]
t0=time.clock()
for i in range(1,20000):
    a.append(i)
print (time.clock() -t0, 'seconds process time')

t0=time.clock()
b=[i for i in range(1,20000)]
print (time.clock() - t0, 'seconds process time')
a=[]
for i in range(1,11):
    a.append(i)

print a

b=[i for i in range(1,11)]
print b

