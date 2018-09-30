distancia = int(input('Informe a distância a ser percorrida na viagem (em km): '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
'''if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45'''
passagem = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('A viagem custará R${:.2f}'.format(passagem))