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
    if n3 == '': #Если шифрованное сообщение пустое - одно из условий не выполнилось
        return 'Error'
    else:
        return n3   
for i in iter(int, 1):
    c = xor(input('Message: '), input('Key: '))
    print('Result =', c)
            

    

    