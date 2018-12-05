#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(md5.hexdigest())

db={
    'michael':'e10adc3949ba59abbe56e057f20f883e',
    'bob':'878ef96e86145580c38c87f0410ad153',
    'alice':'99b1c2188db85afee403b1536010c2c9'
}
def login(user,password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    md5_password=md5.hexdigest()
    return  print(db[user]==md5_password)
if __name__ == '__main__':
    calc_md5('how to use md5 in python hashlib?')
    calc_md5('123456')
    login('michael','123456')
    login('michael','e10aad')