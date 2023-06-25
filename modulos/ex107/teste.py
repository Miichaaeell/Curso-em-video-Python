from ex107 import moedas
p = float(input('Digite um valor: '))
print(f'o Dobro de {p}  é {moedas.dobro(p)}')
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'Com aumento de 10% é {moedas.aumento(p, 10)}')
print(f'Com desconto de 13% é {moedas.diminuir(p, 13)}')