#coding:utf-8

def trapezoid_area(base_up, base_down, height):
    return 1/2.0 * (base_up + base_down)* height

print trapezoid_area(1,2,3)
print trapezoid_area(base_up=1, base_down=2, height=3)

base_up=1
base_down=2
height = 3
print trapezoid_area(height, base_down, base_up)

print('    *', '  **', ' ***', '   |   ')
# print('    *', '  **', ' ***', '   |   ', sep='\n')