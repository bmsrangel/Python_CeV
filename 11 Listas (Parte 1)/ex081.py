# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados
# b) A lista de valores ordenada de forma decrescente
# c) Se o valor 5 foi digitado e está ou não na lista (mostrar a(s) posição(ões) na lista)
num = list()
cont = 0
while True:
    num.append(int(input('Informe o número: ')))
    menu = str(input('Deseja continuar [S/N]? '))
    if menu.lower() in 'nãonao':
        break

num.sort(reverse=True)
print(f'\nForam informados {len(num)} números')
print(f'Os números informados foram: {num}')
if 5 in num:
    for v in num:
        if v == 5:
            cont = cont + 1
    print(f'O número 5 aparece {cont} vezes nas posições ', end='')
    for v in range(0, len(num)):
        if num[v] == 5:
            print(v+1, end=' ')
else:
    print('O número 5 não aparece na lista')