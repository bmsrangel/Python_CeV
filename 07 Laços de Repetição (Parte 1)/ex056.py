media = 0
maiorIdade = 0
totMenor20 = 0

for c in range(1, 5):
    print('====== {}ª PESSOA ======'.format(c))
    nome = str(input('Informe o nome: ')).strip()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip().lower()

    media += idade
    if (idade > maiorIdade) and (sexo == 'm' or sexo == 'masc' or sexo == 'masculino'):
        maiorIdade = idade
        nomeVelho = nome
    if (idade < 20) and (sexo == 'f' or sexo == 'fem' or sexo == 'feminino'):
        totMenor20 += 1

media = media / (c - 1)

print('A média de idade das pessoas informadas é {:.1f} anos'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomeVelho, maiorIdade))
print('De todas as pessoas informadas, {} são mulheres menores de 20 anos'.format(totMenor20))