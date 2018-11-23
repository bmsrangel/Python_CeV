def notas(*args, sit=False):
    """
    Função para cálculo de média
    :param args: notas do aluno
    :param sit: mostrar ou não a situação do aluno
    :return: dicionário com o total de notas informadas, a maior e menor notas, média e situação
    """
    media = 0
    for n in args:
        media += n
    media /= len(args)
    result = {'total': len(args), 'maior': max(args), 'menor': min(args), 'media': media}
    if 0 <= media < 6:
        situacao = 'RUIM'
    elif media < 7:
        situacao = 'RAZOÁVEL'
    elif media < 9:
        situacao = 'BOA'
    else:
        situacao = 'EXCELENTE'
    if sit:
        result['situação'] = situacao
    return result


resp = notas(3.5, 2, 6.5, 7, 2, 4, sit=True)
print(resp)
