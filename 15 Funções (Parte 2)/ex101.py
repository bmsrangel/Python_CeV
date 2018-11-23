from datetime import datetime


def voto(anoNasc):
    global idade
    now = datetime.now()
    idade = now.year - anoNasc
    if idade < 16:
        return 'negado'
    elif idade < 18 or idade > 60:
        return 'opcional'
    else:
        return 'obrigatório'


idade = 0
ano = int(input('Informe o ano de nascimento: '))
sit = voto(ano).upper()
print(f'Com {idade} anos: VOTO {sit}')
