jogador = dict()
gols = list()
soma = 0
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = gols
jogador['total'] = tot
print('-'*45)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-'*45)
print(f'O jogador {jogador["nome"]} jogou {jogador["total"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   o Na partida {i} fez {v} gols')
for g in jogador['gols']:
    soma += g
print(f'Fez um total de {soma} gols')