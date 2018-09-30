numeros = [[], []]
for c in range(0, 7):
    n = int(input(f'Informe o {c+1}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Dos números informados, os números {numeros[0]} são pares e os números {numeros[1]} são ímpares.')