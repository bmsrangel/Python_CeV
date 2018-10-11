from random import randint


def sorteia():
    lst = []
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        lst.append(randint(0, 10))
        print(lst[c], end=' ')
    print('PRONTO!')
    return lst


def somaLista(lst):
    soma = 0
    for l in lst:
        if l % 2 == 0:
            soma += l
    print(f'Somando os valores pares de {lst}, temos {soma}')


lista = []
lista = sorteia()
somaLista(lista)