def metade(preço=0):
    r = preço / 2
    return r


def dobro(preço=0):
    r = preço * 2
    return r


def aumento(preço=0, taxa=0):
    r = preço + (preço * taxa / 100)
    return r


def diminuir(preço=0, taxa=0):
    r = preço - (preço * taxa / 100)
    return r


def moedas(preço=0, moedas='R$'):
   return f'{moedas}{preço:>.2f}'.replace('.', ',')
