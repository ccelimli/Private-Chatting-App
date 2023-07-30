from PasswordCreate import createPassword
from FileEncryption import encryption


def passwordControl():
    password = input('Enter Password: ')
    passwordAgain = input('Please enter the password again: ')
    if password != passwordAgain:
        print('Passwords do not match')
        exit(0)
    else:
        createPassword(password)
        encryption('password.txt')
        pswrd = open('password.txt', 'r')
        return pswrd.read()