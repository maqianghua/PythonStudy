# coding:utf-8
what_he_does = ' play '
his_instrument = ' guitar '
his_name = 'Robert Johnson '
artist_intro = his_name + what_he_does + his_instrument
print (artist_intro)

num = 1
string  = '1'
num2 = int(string )
print (num + num2)

words = 'world' * 3
print(words)

word = 'a loooooong word'
num = 12
string='bang!'
total = string * (len(word) - num) #等价于字符串‘bang!' *4
print (len(word))
print (total)

name = 'My name is Mike'
print(len(name))
print (name[0])
print(name[-4])
print(name[11:14])
print(name[11:15])
print(name[5:])
print(name[:5])#打印的是前五个字符

word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4]+word[-3:-1]
print(find_the_evil_in_your_friends)

url='http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print (file_name)

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search)) + ' to '+ str(num_a.find(search) + len(search)) + 'of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to '+ str(num_b.find(search) + len(search)) + 'of num_b')

print ('{} a word she can get what she {} for .'.format('With', 'came'))
print ('{preposition} a word she can get what she {verb} for '.format(preposition = 'With', verb = 'came'))
print ('{0} a word she can get what she {1} for .'.format('With', 'came'))

# city = input("write down the name of city:")
# url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

lyric_length = len('I cry out for magic')
print(lyric_length)