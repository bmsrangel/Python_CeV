frase = input('Insira uma frase: ').strip().lower()
print('A letra A aparece {} vez(es) na frase informada'.format(frase.count('a')))
print('A primeira vez ocorre na posição {}'.format(frase.find('a')+1))
print('A última vez ocorre na posição {}'.format(frase.rfind('a')+1))
