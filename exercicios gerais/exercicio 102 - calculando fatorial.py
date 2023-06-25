def fatorial(numero, show=False):
    """
    --> Calcula o Fatorial de um número
    :param numero: O valor que vai ser calculado
    :param show: Opcional para mostrar a resolução
    :return: retorna o resultado
    """
    tot = 1
    for c in range(numero, 0 , -1):
        tot *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return print(tot)


help(fatorial)
n = int(input('Deseja ver o Fatorial de qual Numero?'))
while True:
    mostrar = str(input('Deseja ver a resolução do Fatorial? [S/N] ')).upper()
    if mostrar in 'SIM':
        mostrar = True
        break
    elif mostrar in 'NAO':
        mostrar = False
        break
    else:
        print('ERRO!! Digite apenas S ou N')
fatorial(n, mostrar)
