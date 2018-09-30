media = cont = maior = menor = 0
menu = 's'

while menu == 's':
    num = int(input('Insira um número: '))
    media += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    menu = str(input('Deseja continuar [S/N]? ')).strip().lower()

media = media / cont
print('Foram informados {} números. A média entre eles é {:.2f}, o maior número informado foi {} e o menor foi {}'.format(cont, media, maior, menor))