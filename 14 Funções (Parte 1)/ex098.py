from time import sleep
import sys


def linhas():
    print('=-' * 20)


def contador():
    linhas()
    print('Contagem de 1 até 10 de 1 em 1:')
    for c in range(1, 11):
        sleep(0.5)
        print(c, end=' ')
    print('FIM!')
    linhas()
    print('Contagem de 10 até 0 de 2 em 2:')
    for c in range(10, -2, -2):
        sleep(0.5)
        print(c, end=' ')
    print('FIM!')
    linhas()
    print('Contagem personalizada: ')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio <= fim:
        print(f'Contagem de {inicio} a {fim} de {abs(passo)} a {abs(passo)}:')
        for c in range(inicio, fim + 1, abs(passo)):
            sleep(0.5)
            print(c, end=' ')
            # sys.stdout.flush()
    else:
        print(f'Contagem de {fim} a {inicio} de {abs(passo)} a {abs(passo)}:')
        for c in range(inicio, fim + 1, -(abs(passo))):
            sleep(0.5)
            print(c, end=' ')
            # sys.stdout.flush()
    print('FIM!')
    linhas()


contador()
