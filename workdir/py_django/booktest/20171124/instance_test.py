#coding=utf-8

class CocaCola:
    formula=['caffeine', 'sugar', 'water', 'soda']
    def drink(self, how_much):
        if how_much =='a sip':
            print('Cool~')
        elif how_much == 'whole bottle':
            print('Headache!')
ice_coke = CocaCola()
ice_coke.drink('a sip')
