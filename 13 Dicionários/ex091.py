from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'    O {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for c in range(0, 4):
    print(f'    {c+1}º lugar: {ranking[c][0]} com {ranking[c][1]}')