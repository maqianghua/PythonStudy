#coding:utf-8

file=open(r'C:\Users\maqianghua\Desktop\test.txt','w')
file.write('hello wrold')
# file.write('hello wrold')

def text_create(name, msg):
    desktop_path = 'C:\Users\maqianghua\Desktop'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print ('Done')
# text_create(r'\t_hello', 'hello world')#调用函数
def text_filter(word, censored_word = 'lame', changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)
# print text_filter('Python is lame!')#调用函数

def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)
print censored_text_create(r'\try', 'lame!lame!lame!')#调用函数
