valor = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
tempo = int(input('Informe em quantos anos você pretende pagar a casa: '))

parcela = valor / (tempo * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, tempo, parcela))
if (parcela > salario * 0.3):
    print('Empréstimo NEGADO! Salário insuficiente.')
else:
    print('Empréstimo concedido!')
