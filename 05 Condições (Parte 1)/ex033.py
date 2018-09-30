n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if n3 > maior:
    maior = n3

if n3 < menor:
    menor = n3

print('O maior número é {} e o menor número é {}'.format(maior,menor))