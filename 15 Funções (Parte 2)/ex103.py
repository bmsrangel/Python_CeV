def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato')


nome = str(input('Nome do jogador: ')).strip().title()
try:
    gols = int(input('Número de gols: '))
    if not nome.isalpha():
        ficha(gols=gols)
    else:
        ficha(nome, gols)
except ValueError:
    if not nome.isalpha():
        ficha()
    else:
        ficha(nome)
