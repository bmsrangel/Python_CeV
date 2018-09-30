altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura * largura
qtdTinta = area/2
print('Para pintar a parede serão necessários {:.2f} litros de tinta'.format(qtdTinta))