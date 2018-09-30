r1 = float(input('Informe o tamanho do primeiro lado: '))
r2 = float(input('Informe o tamanho do segundo lado: '))
r3 = float(input('Informe o tamanho do terceiro lado: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível montar um triângulo', end=' ')
    if r1 == r2 and r2 == r3:
        print('equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('isósceles')
    else:
        print('escaleno')
else:
    print('Não é possível montar um triângulo')
