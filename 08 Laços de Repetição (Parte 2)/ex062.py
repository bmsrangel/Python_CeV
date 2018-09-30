t0 = int(input('Informe o termo inicial da PA: '))
r = int(input('Informe a razão da PA: '))
cont = 0
qtd = 10
while qtd != 0:
    while cont < qtd:
        t = t0 + cont * r
        cont += 1
        print(t, end=' → ')
    print('Pausa', end='')
    termos = int(input('\nDeseja ver mais quantos termos? '))
    if termos != 0:
        qtd += termos
    else:
        tot = qtd
        qtd = 0
print('\nEncerrando programa... ')
print('Progressão finalizada com {} termos listados'.format(tot))

