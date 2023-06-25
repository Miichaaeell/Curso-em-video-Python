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


def resumo(preço=0, juros=0, desconto=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20} {moedas(preço)}')
    print(f'{"Dobro do preço:":<20} {dobro(preço, True)}')
    print(f'{"Metade do preço:":<20} {metade(preço, True)}')
    print(f'{juros}{"% de aumento:":<18} {aumento(preço, juros, True)}')
    print(f'{desconto}{"% de desconto:":<18} {diminuir(preço, desconto, True)}')
    print('-'*30)