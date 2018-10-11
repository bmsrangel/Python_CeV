# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem utilizar o .sort()). No final, mostre a lista ordenada na tela.
num = list()
for cont in range(0, 5):
    index = 0
    n = (int(input(f'Informe o {cont+1}º número: ')))
    if len(num) == 0:
        num.append(n)
        print('Número inserido no fim da lista!')
    else:
        if n <= num[0]:
            num.insert(0, n)
            print('Número inserido no início da lista!')
        elif n >= num[len(num)-1]:
            num.append(n)
            print('Número inserido no fim da lista!')
        else:
            while n > num[index]:
                index += 1
            num.insert(index, n)
            print(f'Número inserido na posição {index} da lista!')
print(num)