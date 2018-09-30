from time import sleep
from random import randint
computador = randint(0, 10)
cont = 0
acertou = False
print('\n')
print('-=' * 27)
print('Vou pensar num número entre 0 e 10. Tente adivinhar...')
print('-=' * 27)
print('PROCESSANDO...')
sleep(2)
while not acertou:
    n = int(input('Qual o seu palpite? '))
    if computador == n:
        print('\nParabéns!', end=' ')
        acertou = True
    elif n > computador:
        print('Pensei num número menor')
    else:
        print('Pensei num número maior')
    cont += 1

print('Você conseguiu vencer após {} tentativas'.format(cont))