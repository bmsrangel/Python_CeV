salario = float(input('Informe o salário do funcionário: '))
if salario > 1250:
    salario_final = salario * 1.1
else:
    salario_final = salario * 1.15

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,salario_final))