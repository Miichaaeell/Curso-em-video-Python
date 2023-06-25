matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l},{c}: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[l][2] >= 0:
            somacol += matriz[l][2]
print('='*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
#for l in range(0,3):
#    somacol += matriz[l][2]
#for c in range(0, 3):
#    if c == 0:
#        maior = matriz[1][c]
#    elif matriz[1][c] > maior:
#        maior = matriz[1][c]
print('='*30)
print(f'a soma dos numeros pares é {par}')
print(f'a soma dos valores da terceira coluna é {somacol}')
print(f'O maio valor da segunda linha é {maior}')