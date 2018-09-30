n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('O aluno está reprovado')
elif media < 6.9:
    print('O aluno está em recuoeração')
else:
    print('O aluno está aprovado')