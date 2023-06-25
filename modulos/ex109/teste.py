from ex109 import moedas
p = float(input('Digite um valor: '))
print(f'o Dobro de {moedas.moedas(p)}  é {moedas.dobro(p, True)}')
print(f'A metade de {moedas.moedas(p)} é {moedas.metade(p, True)}')
print(f'Com aumento de 10% é {moedas.aumento(p, 10, True)}')
print(f'Com desconto de 13% é {moedas.diminuir(p, 13, True)}')
