print dir(dict)
website={1:"ggoogle","second":"baidu",3:"facebook","twitter":4}
print website.values()
print website.keys()
print website.items()
for key in website.keys():
    print key,type(key)

for key in website:
    print key,type (key)

for k,v in website.items():
    print str(k)+":"+str(v)

print len(website)

new_web=website.copy()
print new_web