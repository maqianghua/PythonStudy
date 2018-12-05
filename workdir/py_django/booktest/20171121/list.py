#coding=utf-8

# all_in_list =[1,              1.0,            'a word',                True,                [1,2],               (1,2),              {'key':'value'}]
# print all_in_list

fruit = ['pineapple', 'pear']
fruit.insert(1, 'grape')
print (fruit)
fruit[0:0] = ['orange']
print(fruit)

fruit = ['pinapple', 'pear', 'grape']
fruit.remove('grape')
print (fruit)

fruit[0] = 'Grapefruit'
print (fruit)

del fruit[0:2]
print (fruit)
