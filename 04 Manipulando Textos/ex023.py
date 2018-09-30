'''num = input('Informe um número entre 0 e 9999: ')
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))'''

num2 = int(input('Informe um número entre 0 e 9999: '))

unidades = num2 % 10
dezenas = num2 // 10 % 10
centenas = num2 // 100 % 10
milhares = num2 // 1000 % 10
print('Unidade: {}'.format(unidades))
print('Dezena: {}'.format(dezenas))
print('Centena: {}'.format(centenas))
print('Milhar: {}'.format(milhares))
