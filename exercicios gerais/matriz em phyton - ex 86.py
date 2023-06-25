'''matriz = [[],[],[]]
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {c}]')))
for c in range(0,3):
    matriz[1].append(int(input(f'Digite um valor para [1, {c}]')))
for c in range(0,3):
    matriz[2].append(int(input(f'Digite um valor para [2, {c}]')))
print('='*30)
for lista in matriz:
    print(f'[ {lista[0]} ] [ {lista[1]} ] [ {lista[2]} ]')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l},{c}: '))
print('='*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()