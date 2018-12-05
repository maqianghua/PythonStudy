#coding:utf-8

class CocaCola():
    formula = ['caffeine', 'sugar', 'water', 'soda']
    def __init__(self):
        # self.local_logo='可口可乐'
        for element in self.formula:
            print('Coke has {}!'.format(element))
    def drink(self): #HERE
        print ('Energy!')
coke=CocaCola()
# print(coke.local_logo)