#coding=utf-8

class CocaCola:
    calories =140
    sodium =45
    total_carb=39
    caffeine=34
    ingredients=[
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]
    def __init__(self, logo_name):
        self.local_log=logo_name
    def drink(self):
        print('You got {} cal energy!'.format(self.calories))

class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients=[
        'High Fructose Corn Syrup',
        "Carbonated Water",
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color'
    ]
coke_a = CaffeineFree('Cocacola-FREE')
coke_a.drink()