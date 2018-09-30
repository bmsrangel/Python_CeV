dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
valor = (60 * dias) + (0.15 * km)
print('O valor total do aluguel é R${:.2f}'.format(valor))