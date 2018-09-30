while True:
    n = int(input('\nInforme um número para ver sua tabuada (insira um número negativo para encerrar): '))
    if n < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 20)
print('Programa encerrado! Volte sempre!')