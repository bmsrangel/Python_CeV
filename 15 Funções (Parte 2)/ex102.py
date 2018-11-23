def fatorial(num, show=False):
    """
    Calcula o fatorial de um número
    :param num: número cujo fatorial será calculado
    :param show: mostrar cálculos
    :return: resultado do cálculo do fatorial
    """
    f = 1
    for c in range(num, f-1, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} = ', end='')
    return f


help(fatorial)
print(fatorial(5, True))
