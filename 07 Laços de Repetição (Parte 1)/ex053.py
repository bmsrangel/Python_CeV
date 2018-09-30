frase = str(input('Informe sua frase: ')).strip().lower()
aux = "".join(frase.split())
cont = 0
for c in range(0, len(aux)):
    if aux[c] == aux[len(aux) - 1 - c]:
        cont += 1

if cont == len(aux):
    print('A frase informada é um palíndromo')
else:
    print('A frase informada não é um palíndromo')