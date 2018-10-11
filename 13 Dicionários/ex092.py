from datetime import datetime
hoje = datetime.now()
pessoa = dict()
pessoa['Nome'] = str(input('Informe o nome: ')).strip()
idade = int(input('Informe o ano de nascimento: '))
pessoa['Idade'] = hoje.year - idade
pessoa['CTPS'] = str(input('Informe o número da CTPS (informe 0 caso não tenha): '))
if pessoa['CTPS'] != '0':
    pessoa['Contratação'] = int(input('Informe o ano de contratação: '))
    pessoa['Salário'] = float(input('Informe seu salário: '))
    pessoa['Idade de aposentadoria'] = pessoa['Contratação'] + 35 - idade
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
