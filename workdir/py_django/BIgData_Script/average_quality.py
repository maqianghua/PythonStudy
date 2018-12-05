#coding:utf-8
from sys import argv

script, quality_file, average_quality_file=argv

in_file=open(quality_file)
out_file=open(average_quality_file, 'w')

line=in_file.readline().strip('\n').split(" ")
str_queryname=line[0]+line[1]
sum_quality=line[2]
while True:
    line = in_file.readline().strip('\n').split(" ")
    if len(line)==0:
        break
    if str_queryname == line[0]+line[1]:
        sum_quality +=line[2]
    else:
        out_file.write(str_queryname+" "+str(sum_quality)+"\n")
        str_queryname = line[0]+line[1]
        sum_quality = line[2]
print "Aright done!"
out_file.close()
in_file.close()