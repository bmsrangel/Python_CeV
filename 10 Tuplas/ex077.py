#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Azedo', 'marrom', 'calçado', 'vermelho', 'gelado', 'mosquito', 'aprender')
vogais = ('a', 'e', 'i', 'o', 'u')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for v in vogais:
        if v in c.lower():
            print(v, end=' ')
