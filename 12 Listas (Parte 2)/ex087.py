cols = list()
lins = list()

for l in range(0, 3):
    for c in range(0, 3):
        cols.append(int(input(f'Informe o número da posição [{l},{c}]: ')))
    lins.append(cols[:])
    cols.clear()
    print('')

soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        if lins[l][c] % 2 == 0:
            soma += lins[l][c]
print(f'A soma de todos os valores pares da matriz é {soma}')

soma = 0
for l in range(0, 3):
    soma += lins[l][2]
print(f'A soma de todos os elementos da terceira coluna é {soma}')
print(f'O maior elemento da segunda linha é {max(lins[1])}')