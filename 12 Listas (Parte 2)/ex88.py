from random import randint
from time import sleep
palpites = list()
numeros = list()
print('-'*60)
print(f'{"Gerador de Palpites":^60}')
print('-'*60)
qtd = int(input('Informe quantos palpites você deseja: '))
for q in range(0, qtd):
    while True:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
        if len(numeros) == 6:
            break
    numeros.sort()
    palpites.append(numeros[:])
    numeros.clear()
print(f'Gerando {qtd} palpites...\n')
sleep(1)
print('-='*30)
print(f'{"Lista de palpites":^60}')
print('-='*30)
for p in range(0, qtd):
    sleep(0.5)
    print(f'Palpite {p+1}: {palpites[p]}')

print('-=' * 30)
print(f'{"Boa sorte!!!":^60}')
print('-='*30)