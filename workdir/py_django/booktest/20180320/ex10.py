#encoding:utf-8
print "I am 6'2\" tall." #将字符串的双引号转义
print 'I am 6\'2" tall.' #将字符串的单引号转义
tabby_cat="\t I'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\ a \\ cat."
fat_cat="""
I 'll do a list:
\t * Cat food
\t * Fishies 
\t * Catnip\n\t * Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
while True:
    for i in ["/", "-","|","\\","|"]:
        print "%s\r" % i,