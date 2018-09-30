maior18 = totH = mulher20 = 0
while True:
    idade = int(input('Informe sua idade: '))
    while idade < 0:
        idade = int(input('Idade inválida! Informe sua idade: '))
    if idade > 18:
        maior18 += 1
    sexo = str(input('Informe seu sexo [M/F]: '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo inválido! Informe se sexo [M/F]: '))
    if sexo in 'Mm':
        totH += 1
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    opção = str(input('Deseja continuar [S/N]? '))
    while opção not in 'SsNn':
        opção = str(input('Opção inválida! Deseja continuar [S/N]? '))
    if opção in 'Nn':
        break

print(f'Foram cadastrados {maior18} pessoas maiores de 18 anos, {totH} homens e {mulher20} mulher(es) abaixo de 20 anos')