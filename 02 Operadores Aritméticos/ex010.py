valor = float(input('Quantos reais você tem na carteira? R$'))
dolar = valor / 3.27
print('Com R${:.2f} é possível comprar US${:.2f}'.format(valor,dolar))