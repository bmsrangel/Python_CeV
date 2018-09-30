#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numerais = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Informe o número entre 0 e 20: '))
    if 0<= num <=20 :
        print(f'O número informado foi o {numerais[num]}')
        menu = str(input('Deseja continuar [S/N]? '))
        if menu.upper() in 'NÃONAO':
            break
    else:
        print('Valor inválido!', end=' ')