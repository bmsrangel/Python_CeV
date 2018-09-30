aluno = dict()
aluno['Nome'] = str(input('Informe o nome do aluno: '))
aluno['Média'] = float(input(f'Informe a média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é {v}')