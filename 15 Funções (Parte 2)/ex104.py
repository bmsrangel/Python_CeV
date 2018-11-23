def leiaInt(entrada=''):
    while True:
        print(entrada, end='')
        n = input()
        if n.isnumeric():
            return n
        else:
            print('Valor inválido!')


n = leiaInt('Informe um número: ')
print(f'Você acabou de digitar o número {n}')
