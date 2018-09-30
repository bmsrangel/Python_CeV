aux = 0

n = int(input('Informe um número: '))
for c in range(1, n+1):
    if n % c == 0:
        aux += 1
        print('\033[1;33m', end='')
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')

if aux == 2:
    print('\n\033[mO número {} é primo'.format(n))
else:
    print('\n\033[mO número {} não é primo'.format(n))