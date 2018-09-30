r1 = float(input('Informe o valor da primeira reta: '))
r2 = float(input('Informe o valor da segunda reta: '))
r3 = float(input('Informe o valor da terceira reta: '))

if (r1 > abs(r2 - r3)) and (r1 < r2 + r3) and (r2 > abs(r1 - r3)) and (r2 < r1 + r3) and (r3 > abs(r1 - r2)) and (r3 < r1 + r2):
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')