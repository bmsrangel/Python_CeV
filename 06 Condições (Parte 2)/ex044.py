print('{:=^40}'.format(' LOJAS RAV '))
valor = float(input('Qual o valor do produto? '))
print("""Formas de pagamento:
1 - À vista no dinheiro ou no cheque
2 - À vista no cartão
3 - Parcelamento em até 2x no cartão
4 - Parcelamento em 3x ou mais no cartão""")
selec = int(input('\nEscolha sua forma de pagamento: '))

if selec == 1:
    valorFinal = valor * 0.9
    print('O total a ser pago é R${:.2f}'.format(valorFinal))
elif selec == 2:
    valorFinal = valor * 0.95
    print('O total a ser pago é R${:.2f}'.format(valorFinal))
elif selec == 3:
    valorFinal = valor
    print('O total a ser pago é R${:.2f} em 2x de R${:.2f}'.format(valorFinal, valorFinal / 2))
elif selec == 4:
    valorFinal = valor * 1.2
    parc = int(input('Informe o número de prestações: '))
    print('O total a ser pago é R${:.2f} em {}x de R${:.2f}'.format(valorFinal, parc, valorFinal / parc))
else:
    print('Opção inválida!')