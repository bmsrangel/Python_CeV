t = int(input('Informe quantos termos da sequencia de Fibonacci você deseja ver: '))
t1 = 0
t2 = 1
cont = 2
print('{} → {}'.format(t1, t2), end=' ')
while cont < t:
   aux = t2
   t2 += t1
   t1 = aux
   cont += 1
   print('→ {}'.format(t2), end=' ')