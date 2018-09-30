print('-' * 20)
print('{:^20}'.format('BANCO BMSR'))
print('-' * 20)
saque = int(input('Qual o valor a ser sacado? R$'))
n50 = saque // 50
n20 = (saque % 50) // 20
n10 = ((saque % 50) % 20) // 10
n5 = (((saque % 50) % 20) % 10) // 5
n1 = (((saque % 50) % 20) % 10) % 5
if n50 != 0:
    print('Notas de R$50,00: {}'.format(n50))
if n20 != 0:
    print('Notas de R$20,00: {}'.format(n20))
if n10 != 0:
    print('Notas de R$10,00: {}'.format(n10))
if n5 != 0:
    print('Notas de R$5,00: {}'.format(n5))
if n1 != 0:
    print('Notas de R$1,00: {}'.format(n1))
print('-' * 20)
print('Obrigado por utilizar nossos caixas eletrônicos! Volte sempre!')