from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano

sexo = str(input('Informe seu sexo [M ou F]: ')).lower()

if sexo == 'f' or sexo == 'fem' or sexo == 'feminino':
    print('Seu alistamento não é obrigatório.', end=' ')
    if idade < 18:
        print('Caso queira se alistar, ainda faltam {} ano(s)'.format(18 - idade))
        tempo = hoje + 18 - idade
        print('Seu alistamento será no ano {}'.format(tempo))
    elif idade > 18:
        print('Como você já tem {} anos, já deveria ter se alistado há {} ano(s)'.format(idade, idade - 18))
        tempo = hoje - (idade - 18)
        print('Seu alistamento foi no ano {}'.format(tempo))
    else:
        print('Você já pode se alistar')
elif sexo == 'm' or 'masc' or 'masculino':
    if idade < 18:
        print('Você tem {} anos e ainda faltam {} ano(s) para seu alistamento'.format(idade, 18 - idade))
        tempo = hoje + 18 - idade
        print('Seu alistamento será no ano {}'.format(tempo))
    elif idade > 18:
        print('Você tem {} anos e já deveria ter se alistado há {} ano(s)'.format(idade, idade - 18))
        tempo = hoje - (idade - 18)
        print('Seu alistamento foi no ano {}'.format(tempo))
    else:
        print('Você tem que se alistar IMEDIATAMENTE')