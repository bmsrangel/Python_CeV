# Desenvolva um programa que leia quatro valores pelo teclado s guarde-os em uma tupla. No final, mostre:
# a) quantas vezes apareceu o valor 9
# b) em que posição foi digitado o primeiro valor 3
# c) Quais foram os números pares

numeros = (int(input('Informe um número: ')),
           int(input('Informe outro número: ')),
           int(input('Informe mais um número: ')),
           int(input('Informe o último número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 aparece pela primeira vez na {numeros.index(3)+1}ª posição')
else:
    print('O número 3 não foi informado')
print('Os seguintes números informados são pares: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')