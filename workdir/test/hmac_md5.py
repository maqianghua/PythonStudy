#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hmac, random
db={}
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),'md5').hexdigest()

class User(object):
    def __init__(self,username, password):
        self.username=username
        # random,randint(48,122)
        # 随机生成大于等于48小于等于122的整数
        # chr(random,randint(48,122))
        # 生成对应随机数的ascii码对应的字符
        # [chr(random,randint(48,122)) for i in range(20)]
        # 列表生成器，其中有20个元素，每个元素字符都是ascii码48到122之间的随机字符
        # ''.join([chr(random.randint(48,122)) for i in range(20)])
        # 返回一个以分隔符''连接各个元素后生成的字符串
        self.key=''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password=hmac_md5(self.key, password)

def register(username, password):
    db[username]=User(username, password)

def login(username, password):
    user=db[username]
    return user.password == hmac_md5(user.key, password)

register('michael','123456')
register('bob','abc999')
assert not login('michael','1234567')
assert not login('bob','123456')
print ('ok')