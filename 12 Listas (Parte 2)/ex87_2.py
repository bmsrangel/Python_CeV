matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spares = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número da posição [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spares += matriz[l][c]
    somacol += matriz[l][2]
    print()
print(f'A soma de todos os números pares da matriz é {spares}')
print(f'A soma de todos os elementos da segunda coluna é {somacol}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
