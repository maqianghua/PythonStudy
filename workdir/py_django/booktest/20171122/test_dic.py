# coding=utf-8
NASDAQ_code = {
    'BIDU':'Baidu',
    'SINA':'Sina'
    # 'YOKU':'YouKu'
    # 'BIDU':

}
# print NASDAQ_code
# key_test = {[]: 'a Test'}
# print (key_test)
# a = {'key':123, 'key':123}
# print (a)
NASDAQ_code['YOKU']='Youku'
print (NASDAQ_code)

NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
print (NASDAQ_code)
del NASDAQ_code['FB']
print (NASDAQ_code)
NASDAQ_code['TSLA']
