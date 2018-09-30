from random import randint
vitórias = 0
print('=-' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 12)
while True:
    computador = randint(0, 5)
    jogador = int(input('Jogue seu número: '))
    while True:
        opção = str(input('Par ou Ímpar [P/I]? '))
        if opção in 'PpIi':
            break
        else:
            print('Opção inválida!', end=' ')
    total = computador + jogador
    if total % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'ímpar'
    print('-' * 70)
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total das jogadas ({total}) é {resultado.upper()}')
    print('-' * 70)
    if (computador + jogador) % 2 == 0:
        print('=' * 12)
        print('Você ganhou!\nVamos jogar novamente...')
        vitórias += 1
    else:
        print('=' * 12)
        print('Você perdeu!')
        break
print('~' * 33)
print(f'Total de vitórias consecutivas: {vitórias}')