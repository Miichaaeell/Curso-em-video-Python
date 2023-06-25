from time import sleep
from random import randint
palpites= list()
contador = 0
quantia = int(input('Quantos jogos você quer que eu sorteie?'))
print(f'Sorteando {quantia} Jogos')
for j in range(0,quantia):
    while True:
        n = randint(0, 60)
        if n not in palpites:
            palpites.append(n)
            contador += 1
        if contador >= 6:
            break
    print(f'Jogo {j + 1}: {sorted(palpites)}')
    palpites.clear()
    contador = 0
    sleep(1)
print('===Boa Sorte===')