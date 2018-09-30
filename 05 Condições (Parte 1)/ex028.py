import random
from time import sleep
num = random.randint(0,5) #Faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
palpite = int(input('Em que número pensei? '))
print('Processando...')
sleep(3)
print('Parabéns! Você conseguiu me vencer!' if num == palpite else 'Você perdeu! Eu pensei no número {} e não no número {}'.format(num,palpite))