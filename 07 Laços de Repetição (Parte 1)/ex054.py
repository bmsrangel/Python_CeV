from datetime import date
totMenor = 0
totMaior = 0

for c in range(1, 8):
    n = int(input('Informe a data de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - n
    if idade >= 21:
        totMaior += 1
    else:
        totMenor += 1

print('De todas as pessoas informadas, {} já são maiores de idade e {} ainda são menores de idade'.format(totMaior, totMenor))