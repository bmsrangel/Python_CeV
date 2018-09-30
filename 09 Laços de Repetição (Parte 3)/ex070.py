totalCompra = qtd1000 = cont = 0

while True:
    prod = str(input('Informe o nome do produto: '))
    preço = float(input('Informe o preço do produto: R$'))
    while preço < 0:
        preço = float(input('Preço inválido! Informe o preço correto do produto: R$'))
    totalCompra += preço
    if preço > 1000:
        qtd1000 += 1
    if cont < 1:
        nomeBarato = prod
        preçoBarato = preço
    elif preço < preçoBarato:
        preçoBarato = preço
        nomeBarato = prod
    cont += 1
    opção = str(input('Deseja continuar [S/N]? '))
    while opção not in 'SsNn':
        opção = (str(input('Opção inválida! Deseja continuar [S/N]? ')))
    if opção in 'Nn':
        break

print('Valor total da compra: R${:.2f}'.format(totalCompra))
print('Número de produtos que custam mais de R$1000,00: {}'.format(qtd1000))
print('Nome do produto mais barato: {}'.format(nomeBarato.capitalize()))
