pessoas = list()
aux = list()
while True:
    aux.append(str(input('Informe o nome: ')))
    aux.append(float(input('Informe o peso: ')))
    pessoas.append(aux[:])
    aux.clear()
    menu = str(input('Deseja continuar [S/N]? '))
    if menu.lower() in 'nãonao':
        break
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
listaPesadas = list()
listaLeves = list()
for p in pessoas:
    if p[1] >= 100:
        listaPesadas.append(p[0])
    if p[1] <= 70:
        listaLeves.append(p[0])
print(f'As pessoas mais pesadas são {listaPesadas}')
print(f'As pessoas mais leves são {listaLeves}')