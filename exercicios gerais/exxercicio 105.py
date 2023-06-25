def notas(*num, sit=False):
    """
    Função para avaliar notas e situação de varios alunos
    :param num:As notas do aluno
    :param sit:Opcional para mostrar a situação do aluno ou não
    :return:dicionário com as informações sobre o aluno
    """
    resultado = {}
    resultado['total'] = len(num)
    resultado['maior'] = max(num)
    resultado['menor'] = min(num)
    resultado['média'] = sum(num) / len(num)
#    maior = 0
#    for n in num:
#        if n > maior:
#            maior = n
#    resultado['maior'] = maior
#    menor = 0
#    for p, n in enumerate(num):
#        if p == 0:
#            menor = n
#        elif n < menor:
#            menor = n
#    resultado['menor'] = menor

    if sit:
        if resultado['média'] < 5:
            resultado['situação'] = 'Ruim'
        elif resultado['média'] > 5 and resultado['média'] < 7:
            resultado['situação'] = 'Razoavel'
        elif resultado['média'] > 7:
            resultado['situação'] = 'Boa'
    return resultado

resultado = notas(5.5, 2.5, 1.5, sit=True)
print(resultado)



