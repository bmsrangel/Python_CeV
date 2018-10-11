time = list()
jogador = dict()
gols = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    time.append(jogador.copy())
    gols.clear()
    menu = str(input('Deseja continuar [S/N]? '))
    if menu.lower() in 'nãonao':
        break
print('-='*30)
print(f'{"cod":^3}{"Nome":^10}{"Gols":^20}{"Total de gols":^17}')
print('-'*60)
for i, t in enumerate(time):
    soma = 0
    for g in jogador['gols']:
        soma += g
    print(f'{i:^3}{t["nome"]:^10}{str(t["gols"]):^20}{soma:^17}')
print('-'*60)
while True:
    menu = int(input('Mostrar levantamento de qual jogador (999 para encerrar)? '))
    if menu != 999:
        if menu < len(time):
            print(f'-- LEVANTAMENTO DO JOGADOR {time[menu]["nome"]} --')
            for i, g in enumerate(time[menu]["gols"]):
                print(f'   o No jogo {i} fez {g} gols.')
        else:
            print('Jogador não encontrado!')
        print('-' * 60)
    else:
        print('Encerrando programa... \n<<VOLTE SEMPRE>>')
        break