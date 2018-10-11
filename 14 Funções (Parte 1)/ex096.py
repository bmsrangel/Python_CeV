def área(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é {area:.1f}m²')


print(f'{"Controle de Terrenos":^30}')
print('-'*30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
área(largura, comprimento)