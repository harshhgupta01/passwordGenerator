import random

print('Welcome to Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><?0123456789'

number = int(input('Number of passwords to generate: '))
length = int(input('Your password length: '))

print('\nHere are your password:')

for i in range(number):
    passwords = ''
    for j in range(length):
        passwords += random.choice(chars)
    print(passwords)
