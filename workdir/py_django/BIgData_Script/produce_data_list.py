#coding:utf-8
from sys import argv
from os.path import exists
script,from_file, to_file=argv

in_file=open(from_file)
sum_rows = -1
for sum_rows, line in enumerate(open(from_file, 'rU')):
   pass
sum_rows += 1
#sum_rows=int(total_rows)
pre_string="${ssentieon}/bwa mem -M -R '@RG\\tID:${sampleid}\\tPL:COMPLETE\\tLB:${sampleid}_num\\tSM:${sampleid}\\tCN:BGI' " \
           "${href}"
result=""
tail=" && "
count=1
library_num=1
while True:
    line=in_file.readline().strip('\n')
    if (sum_rows ==1):
        str_lib_num = str(library_num)
        result = result + pre_string.replace("num", str_lib_num) + line
        break
    if (count%2 == 1 ):
        str_lib_num = str(library_num)
        result =result+pre_string.replace("num",str_lib_num)+line
    elif (count < sum_rows):
        result = result + line+tail
    elif (count == sum_rows):
        result = result + line
        break
    if (count%2 ==0):
        library_num +=1
    count +=1


out_file=open(to_file, 'w')
out_file.write(result)

out_file.close()
in_file.close()