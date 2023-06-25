import moedas
p = float(input('Digite um valor: '))
print(f'o Dobro de {moedas.moedas(p)}  é {moedas.moedas(moedas.dobro(p))}')
print(f'A metade de {moedas.moedas(p)} é {moedas.moedas(moedas.metade(p))}')
print(f'Com aumento de 10% é {moedas.moedas(moedas.aumento(p, 10))}')
print(f'Com desconto de 13% é {moedas.moedas(moedas.diminuir(p, 13))}')
