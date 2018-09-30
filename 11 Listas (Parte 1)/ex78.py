# Faça um programa que leia 5 valores numéricos e guarde-os numa lista.
# No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posições na lista.
numeros = list()
for cont in range(0, 5):
    numeros.append(int(input(f'Informe o {cont+1}º número: ')))

print(f'Os números informados foram {numeros}')
print(f'O maior valor é {max(numeros)} e encontra-se na posição ', end='')
for pos, cont in enumerate(numeros):
    if cont == max(numeros):
        print(pos, end=' ')
print(f'\nO menor valor é {min(numeros)} e encontra-se na posição ', end='')
for pos, cont in enumerate(numeros):
    if cont == min(numeros):
        print(pos, end=' ')