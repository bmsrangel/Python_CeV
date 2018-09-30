#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois, mostre:
#a) os 5 primeiros colocados
#b) os 4 últimos colocados
#c) Uma lista com os times em ordem alfabética
#d) Em que posição da tabela está o time do Chapecoense
classificacao = ('São Paulo', 'Internacional', 'Palmeiras', 'Flamengo', 'Grêmio', 'Atlético', 'Cruzeiro', 'Corinthians',
                 'Santos', 'Fluminense', 'Atlético-PR', 'América-MG', 'EC Vitória', 'Bahia', 'Botafogo', 'Ceará SC',
                 'Vasco da Gama', 'Chapecoense', 'Sport Recife', 'Paraná')

print('=-'*50)
print(f'Os cinco primeiros colocados são: {classificacao[:5]}')
print('=-'*50)
print(f'Os quatro últimos colocados são: {classificacao[-4:]}')
print('=-'*50)
print(f'Lista de times em ordem alfabética: {sorted(classificacao)}')
print('=-'*50)
print(f'O Chapecoense está em {classificacao.index("Chapecoense")+1}º lugar')
