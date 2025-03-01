from vernam import xor
import random
for i in iter(int, 1):
    op = input("1 - Encrypt, 2 - Decrypt ")
    if op == '1':
        keytype = input('1 - your key, 2 - random key ')
        if keytype == '1':
            c = xor(input('Message: '), input('Key: '))
            print('Result =', c)
        elif keytype == '2':
            randomkey = ''
            message = input('Message: ')
            for i in range(len(message)):
                randomkey += str(random.randint(0, 1))
            c = xor(message, randomkey)
            print('Key = ', randomkey)
            print('Result = ', c)
    elif op == '2':
        c = xor(input('Cipher-text: '), input('Key: '))
        print('Result =', c)
