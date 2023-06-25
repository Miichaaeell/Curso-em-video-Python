def metade(preço=0, formatado=False):
    r = preço / 2
    return r if formatado is False else moedas(r)


def dobro(preço=0, formatado=False):
    r = preço * 2
    return r if formatado is False else moedas(r)


def aumento(preço=0, taxa=0, formatado=False):
    r = preço + (preço * taxa / 100)
    return r if formatado is False else moedas(r)


def diminuir(preço=0, taxa=0, formatado=False):
    r = preço - (preço * taxa / 100)
    return r if not formatado else moedas(r)


def moedas(preço=0, moedas='R$'):
   return f'{moedas}{preço:.2f}'.replace('.', ',')
