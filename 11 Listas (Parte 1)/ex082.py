# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
valores = list()
pares = list()
impares = list()

while True:
    valores.append(int(input('Informe um número: ')))
    menu = str(input('Deseja continuar [S/N]? '))
    if menu.lower() in 'nãonao':
        break
for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Os números informados foram: {valores}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')