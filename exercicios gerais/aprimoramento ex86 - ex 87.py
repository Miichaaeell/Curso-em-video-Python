matriz = [[],[],[]]
soma = pares = maior = 0
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]')))
for c in range(0,3):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]')))
for c in range(0,3):
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]')))
print('='*30)
for lista in matriz:
    print(f'[ {lista[0]} ] [ {lista[1]} ] [ {lista[2]} ]')
    soma += lista[2]
print('='*30)
for n in matriz[0]:
    if n % 2 == 0:
        pares += n
for n in matriz[1]:
    if n % 2 == 0:
        pares += n
    if n > maior:
        maior = n
for n in matriz[2]:
    if n % 2 == 0:
        pares += n
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')