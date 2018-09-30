cols = list()
lins = list()

for l in range(0, 3):
    for c in range(0, 3):
        cols.append(int(input(f'Informe o número da posição [{l},{c}]: ')))
    lins.append(cols[:])
    cols.clear()
    print('')
for l in range(0, 3):
    for c in range(0,3):
        print(lins[l][c], end=' ')
    print('')