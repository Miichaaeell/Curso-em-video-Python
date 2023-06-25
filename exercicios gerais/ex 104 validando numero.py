def leiaint(txt):
    while True:
        n = str(input(f'{txt}'))
        if n.isnumeric():
            return n
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

n = leiaint('Digite um numero: ')
print(f'Você digitou o número {n}')