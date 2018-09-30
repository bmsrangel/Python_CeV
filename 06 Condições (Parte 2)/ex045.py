#Exercício 045
import random
import emoji

lista = ['pedra', 'papel', 'tesoura']

computador = random.choice(lista)

jogador = str(input('Informe sua jogada (pedra, papel ou tesoura): ')).lower().strip()

print('Sua jogada: \033[1;4;34m{}\033[m'.format(jogador.upper()))
print('Jogada do computador: \033[1;4;35m{}\033[m'.format(computador.upper()))

if computador == 'pedra':
    if jogador == 'pedra':
        print(emoji.emojize('\033[1;4;33mEmpatou\033[m :open_mouth:', use_aliases = True))
    elif jogador == 'papel':
        print(emoji.emojize('Você \033[1;4;32mGANHOU!!!\033[m :clap:', use_aliases = True))
    else:
        print(emoji.emojize('Você \033[1;4;31mperdeu\033[m :cry:', use_aliases = True))
elif computador == 'papel':
    if jogador == 'pedra':
        print(emoji.emojize('Você \033[1;4;31mperdeu\033[m :cry:', use_aliases = True))
    elif jogador == 'papel':
        print(emoji.emojize('\033[1;4;33mEmpatou!\033[m :open_mouth:', use_aliases = True))
    else:
        print(emoji.emojize('Você \033[1;4;32mGANHOU!!!\033[m :clap:', use_aliases = True))
else:
    if jogador == 'pedra':
        print(emoji.emojize('Você \033[1;4;32mGANHOU!!!\033[m :clap:', use_aliases = True))
    elif jogador == 'papel':
        print(emoji.emojize('Você \033[1;4;31mperdeu\033[m :cry:', use_aliases = True))
    else:
        print(emoji.emojize('\033[1;4;33mEmpatou!\033[m :open_mouth:', use_aliases = True))
