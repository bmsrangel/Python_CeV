peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)
if imc < 18.5:
    cat = 'abaixo do peso'
elif imc < 25:
    cat = 'no peso ideal'
elif imc < 30:
    cat = 'em sobrepeso'
elif imc < 40:
    cat = 'obeso'
else:
    cat = 'em obesidade mórbida'
print('Seu IMC é {:.1f} e você está {}'.format(imc, cat))
