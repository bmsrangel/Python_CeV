pessoas = list()
individuo = dict()
media = 0
while True:
    individuo['nome'] = str(input('Nome: ')).strip().capitalize()
    individuo['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    individuo['idade'] = int(input('Idade: '))
    pessoas.append(individuo.copy())
    menu = str(input('Deseja continuar [S/N]? '))
    if menu.lower() in 'nãonao':
        break
print(pessoas)
print('-='*25)
print(f'Foram cadastradas {len(pessoas)} pessoas')
for p in pessoas:
    media += p['idade']
media = media/len(pessoas)
print(f'A média de idade é {media:.0f} anos')
print('Lista das mulheres cadastradas: ')
if not 'F' in pessoas:
    print('   o Nenhuma mulher cadastrada')
else:
    for p in pessoas:
        if p['sexo'] == 'F':
            print('   o', p['nome'])
print('Pessoas acima da média de idade: ')
if len(pessoas) == 1:
    print(f'   o Só existe 1 pessoa cadastrada e sua idade é {pessoas[0]["idade"]}')
else:
    for p in pessoas:
        if p['idade'] > media:
            print('   o', p['nome'])