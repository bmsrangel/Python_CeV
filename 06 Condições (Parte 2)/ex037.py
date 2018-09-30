print('*-' * 20)
print('Programa de conversão de bases numéricas')
print('*-' * 20)
num = int(input('\nInforme um número a ser convertido: '))
print("""As opções de conversão são as seguintes:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal""")
opcao = int(input('\nInforme sua opção: '))

if opcao == 1:
    print('O número {} em binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} em octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')

input('\nPressione qualquer tecla para continuar...')