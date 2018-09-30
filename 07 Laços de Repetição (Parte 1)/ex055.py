maiorPeso = 0
menorPeso = 0

for c in range(0, 5):
    peso = float(input('Informe seu peso: '))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print('O maior peso informado foi {:.1f}kg e o menor peso informado foi {:.1f}kg'.format(maiorPeso, menorPeso))
