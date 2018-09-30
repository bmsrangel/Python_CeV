velocidade = int(input('Informe a velocidade do carro (em km/h): '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Limite de velocidade excedido!!! Você foi multado em R${:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')