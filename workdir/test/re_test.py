

import re

# patt=re.compile(r'^([a-zA-Z0-9\.]+)@([a-zA-Z]+)\.(\w{2,3})')
patt=re.compile(r'^([\w\_\.]+?)@(\w+?\.[a-zA-Z]+)$')

def is_valid_email(addr):
    if patt.match(addr):
        return True
    else:
        return False
patt_2=re.compile(r'^\<?([\w\s]*?)\>?\s?([\w\.\_]+?)@(\w+\.[a-zA-Z]+)$')
def name_of_email(addr):
    m=patt_2.match(addr)
    if m:
        if m.group(1):
            return m.group(1)
        else:
            return m.group(2)
    else:
        return False
if __name__ == '__main__':
    #测试版本1
    assert is_valid_email('someone@gmail.com')
    assert is_valid_email('bill.gates@microsoft.com')
    assert not is_valid_email('bob#example.com')
    assert not is_valid_email('mr-boob@example.com')
    print('ok')
    #测试版本2
    assert name_of_email('<Tom Paris> tom@voyager.org')=='Tom Paris'
    assert name_of_email('tom@voypager.org')=='tom'
    print('ok')