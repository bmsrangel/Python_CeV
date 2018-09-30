n = acum = cont = 0
while n != 999:
    n = int(input('Informe um número (informe 999 para encerrar): '))
    if n != 999:
        acum += n
        cont += 1

print('A soma dos {} números informados é {}'.format(cont, acum))
