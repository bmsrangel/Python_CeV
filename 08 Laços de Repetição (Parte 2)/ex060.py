n = int(input('Qual número você deseja calcular o fatorial? '))
if n == 0:
    print('Por definição, 0! = 1')
else:
    fat = 1
    cont = n
    print('{}! ='.format(n), end=' ')
    while cont >= 1:
        if cont > 1:
            print('{} x'.format(cont), end=' ')
        else:
            print('{}'.format(cont), end=' ')
        fat *= cont
        cont -= 1

    print('= {}'.format(fat))
'''
n = int(input('Qual número você deseja calcular o fatorial? '))
fat = 1
if n == 0:
    print('Por definição, 0! = 1')
else:
    print('{}! ='.format(n), end=' ')
    for c in range(n, 0, -1):
        fat *= c
        if c > 1:
            print('{} x'.format(c), end=' ')
        else:
            print('{}'.format(c), end=' ')

    print('= {}'.format(fat))
'''