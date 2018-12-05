from sys import argv
script, first, second, third =argv
age=raw_input("How old are you? ")
height=raw_input("HOw tall are you? ")
weight=raw_input("How much do you weight? ")
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable id:", second
print "YOur third variable id:", third
print "So, you're %r old, %r tall and %r heavy." % (age,height,weight)