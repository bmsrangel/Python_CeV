cores = {'limpa': '\033[m', 'cabeçalho': '\033[1;30;42m',
         'acesso': '\033[1;30;44m', 'ajuda': '\033[7;30m',
         'encerramento': '\033[1;30;41m'}


def cabeçalho():
    print('{}{}'.format(cores['cabeçalho'], '~') * 60)
    print(f'{"SISTEMA DE AJUDA PyHELP":^60}')
    print('~' * 60)
    print(cores['limpa'], end='')


def ajuda(comando):
    print('{}{}'.format(cores['acesso'], '~') * 60)
    frase = f"Acessando o manual do comando '{comando}'"
    print(f'{frase:^60}')
    print('~' * 60)
    print(cores['ajuda'], end='')


def fim():
    print('{}{}'.format(cores['encerramento'], '~') * 60)
    print(f'{"ATÉ LOGO":^60}')
    print('~' * 60)
    print(cores['limpa'], end='')


while True:
    cabeçalho()
    com = str(input('Função ou Biblioteca > ')).lower()
    if com not in 'fim':
        ajuda(com)
        help(com)
    else:
        fim()
        break
