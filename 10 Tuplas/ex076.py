# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular
produtos = ('Sabão', 5.6, 'Arroz', 9.8, 'Pasta de dente', 1.5, 'Celular', 1100)
print('-'*60)
print(f'{"Tabela de Preços":^60}')
print('-'*60)
for c in range(0, len(produtos),2):
    print(f'{produtos[c]:.<49}R${produtos[c+1]:>8.2f}')