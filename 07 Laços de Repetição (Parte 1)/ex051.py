t0 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))

#for c in range(0, 10):
#    print('{}° termo da PA: {}'.format(c + 1, t0 + c * r))
aux = 1
for c in range(t0, t0 + 10 * r, r):
    print('{}° termo da PA: {}'.format(aux, c))
    aux += 1