
class CocaCola:
    formula =['caffeine', 'sugar', 'water', 'soda']

coke_for_me = CocaCola()
coke_for_you = CocaCola()
print (CocaCola.formula)
print (coke_for_me.formula)
print (coke_for_you.formula)
for element in coke_for_me.formula:
    print (element)
