import math
valor = float(input('Digite um ângulo qualquer: '))
ang = math.radians(valor)
print('O seno de {}° é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(valor,math.sin(ang),math.cos(ang),math.tan(ang)))