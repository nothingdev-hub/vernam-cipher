import random
def xor(n1, n2):
    flaglen = False 
    flagsym = True
    n3 = ""
    if len(n1) == len(n2): #Проверяем длину сообщений
        flaglen = True
        if flaglen:
            for i in range(len(n1)):
                if n1[i] != '0' and n1[i] != '1' or n2[i] != '0' and n2[i] != '1': #Проверяем наличие в сообщениях лишних символов
                    flagsym = False
    if flagsym and flaglen: 
        for i in range(len(n1)): #Проводим xor операцию по индексам
            if n1[i] == n2[i]: 
                n3 += '0'
            else:
                n3 += '1'
    if n3 == '': #Если шифрованное или дешифрованное сообщение пустое - одно из условий не выполнилось
        return 'Error'
    else:
        return n3   
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
            print('Reuslt = ', c)
    elif op == '2':
        c = xor(input('Cipher-text: '), input('Key: '))
        print('Result =', c)
        
    
    

    

    
