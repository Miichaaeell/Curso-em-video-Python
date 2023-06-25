from random import randint
from time import sleep
def linha():
    print('-' * 37)
def sorteia(n, lista):
    print(f'Sorteando {n} valores " ', end=' ')
    for c in range(0, n):
        v = randint(0, 10)
        sleep(0.5)
        print(f'{v}', end=' ')
        lista.append(v)
    print('" Pronto!')
def somapar(lista):
    s = 0
    print(f'Somando os valores pares sorteados "', end=' ')
    for n in lista:
        if n % 2 == 0:
            s += n
            print(f'{n}', end=' ')
    print(f'" temos {s}')
def somaimpar(lista):
    s = 0
    print(f'Somando os valores ímpares sorteados "', end=' ')
    for n in lista:
        if n % 2 != 0:
            s += n
            print(f'{n}', end=' ')
    print(f'" Temos {s}')
def somatotal(lista):
    print(f'A soma de todos os números da lista {lista} é {sum(lista)}')
def menu():
    print('-'*15, 'MENU', '-'*15)
    print('1 - Soma dos números pares')
    print('2 - soma dos números ímpares')
    print('3 - Soma total dos números sorteados')
    print('4 - Sortear novos números')
    print('9 - para sair')
    linha()
    while True:
        pergunta = int(input('O que deseja fazer? '))
        if pergunta > 0 and pergunta <= 4 or pergunta == 9:
            break
        else:
            print(f'ERRO! O valor {pergunta} não faz parte das opções')
    return(pergunta)

numeros = []
while True:
    quantia = int(input('Quantos valores deseja sortear ? '))
    sorteia(quantia, numeros)
    while True:
        resposta = menu()
        if resposta == 1:
            somapar(numeros)
        elif resposta == 2:
            somaimpar(numeros)
        elif resposta == 3:
            somatotal(numeros)
        elif resposta == 4 or resposta == 9:
            break
    numeros.clear()
    if resposta == 9:
        break
linha()
print('ENCERRANDO O PROGRAMA, VOLTE SEMPRE !')
