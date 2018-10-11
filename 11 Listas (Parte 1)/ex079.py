# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já existe lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos
# digitados, em ordem crescente.

numero = list()
while True:
    n = int(input('Informe um número: '))
    if n in numero:
        print('O número já existe na lista!')
    else:
        numero.append(n)
    menu = str(input('Deseja continuar [S/N]? '))
    if menu.lower() in 'nãonao':
        break
numero.sort()
print(f'Os valores digitados foram {numero}')