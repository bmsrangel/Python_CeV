# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input('Informe sua expressão: '))
pilha = list()
for e in expressao:
    if e == '(':
        pilha.append(e)
    elif e == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(e)
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Expressão incorreta!')