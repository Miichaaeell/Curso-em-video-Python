from time import sleep
def linha():
    print('-='*15)
def contador(a, b, c):
    linha()
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print(f'Contando de {a} até {b} de {c} em {c} ')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont += c
        print('FIM')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont -= c
        print('FIM')
contador(0, 10, 1)
contador(10, -4, -2)
linha()
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)
