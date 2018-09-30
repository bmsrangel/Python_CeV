menu = 0
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
while menu != 5:
    print("""O que você gostaria de fazer com os números informados? 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Inserir novos números
    [ 5 ] Encerrar programa""")
    menu = int(input('\nInforme sua opção: '))
    if menu == 1:
        print('A soma dos números informados é {}'.format(n1 + n2))
    elif menu == 2:
        print('O produto dos números informados é {}'.format(n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('O primeiro número ({}) é maior que o segundo número ({})'.format(n1, n2))
        elif n1 < n2:
            print('O segundo número ({}) é maior que o primeiro número ({})'.format(n2, n1))
        else:
            print('Os números informados são iguais')
    elif menu == 4:
        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))
    elif menu == 5:
        print('Encerrando programa...')
    else:
        print('Opção inválida! Tente novamente!')