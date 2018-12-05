#coding=utf-8

# def account_login():
#     password = input('Password:')
#     if password == '12345':
#         print ('Login sucsess!')
#     else:
#         print (' wrong password or invalid input! ')
#         account_login()
def account_login():
    password = input('Password:')
    password_correct = password == '12345'  #here!
    if password_correct:
        print ('login success!')
    else:
        print ('Wrong password or invalid input! ')
        account_login()
account_login()