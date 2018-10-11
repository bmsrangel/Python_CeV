turma = list()
aluno = list()
notas = list()

while True:
    aluno.append(str(input('Informe o nome do aluno: ')))
    notas.append(float(input('Informe a primeira nota: ')))
    notas.append(float(input('Informe a segunda nota: ')))
    media = (notas[0] + notas[1]) / 2
    aluno.append(notas[:])
    aluno.append(media)
    turma.append(aluno[:])
    aluno.clear()
    notas.clear()
    menu = str(input('Deseja continuar [S/N]? '))
    if menu.lower() in 'nãonao':
        print('')
        break
    else:
        print('')
print('='*20)
print(f'{"Relatório de Notas":^20}')
print('='*20)
print(f'{"No.":^3}{"Nome":<12}{"Média":^5}')
print('-'*20)
for cont in range(0, len(turma)):
    print(f'{cont+1:^5}{turma[cont][0]:<12}{turma[cont][2]:^5.1f}')
print()
while True:
    num = int(input('Para ver a nota de um aluno específico, digite o número (ou 999 para encerrar): '))
    if num != 999:
        print(f'As notas de {turma[num-1][0]} foram {turma[num-1][1]}')
    else:
        print('Encerrando o programa...\n<<<VOLTE SEMPRE>>>')
        break
