#coding:utf-8
from math import sqrt
def fahrenheit_converter(C):
    fahrenheit = C * 9/5 + 32
    return str(fahrenheit) + '°F'
C2F = fahrenheit_converter(35)
print (C2F)

def g_convert_kg(C):
    num_kg = C/1000.0
    return str(num_kg) + 'kg'
g2kg=g_convert_kg(100023)
print (g2kg)

def bevel_length(a,b):
    bevel = (a^2.0+b^2.0)^0.5
    bevel2 = (a**2.0+b**2.0)**0.5
    # bevel3=numpy.sqrt(a^2+b^2)
    bevel1=sqrt(a^2+b^2)
    # print (%d,%d, %d,%d )% (bevel,bevel1,bevel2,bevel3)
    return (bevel,bevel2,bevel1)
(bevel_result1,bevel_result2,bevel_result3) = bevel_length(3,4)
print (bevel_result1,bevel_result2,bevel_result3)