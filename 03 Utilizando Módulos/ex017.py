import math
cat1 = float(input('Informe o cateto oposto: '))
cat2 = float(input('Informe o cateto adjacente: '))

#hip = math.sqrt(pow(cat1,2)+pow(cat2,2))
hip = math.hypot(cat1, cat2)

print('A hipotenusa do triângulo mede {:.2f}'.format(hip))