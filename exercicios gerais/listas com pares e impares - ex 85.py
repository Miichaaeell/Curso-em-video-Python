numeros = [[],[]]
for c in range (0, 7):
    n = int(input(f'Digite o {c + 1}º numero:'))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)


print(f'Os números pares são {sorted(numeros[0])}')
print(f'Os números impares são {sorted(numeros[1])}')

