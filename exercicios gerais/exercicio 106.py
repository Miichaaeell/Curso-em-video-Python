'''def linha(msg):
    print('~' * (len(msg)))
    print(f'{msg:>3}')
    print('~' * (len(msg)))
while True:
    print('\033[:42m', end='')
    linha('SISTEMA DE AJUDA PyHELP')
    ajuda = str(input('\033[:45mBiblioteca ou Função > ')).lower()
    print('\033[:44m', end='')
    if ajuda in 'fim':
        break
    linha(f"Acessando o manual do comando '{ajuda}'")
    print('\033[1:30:47m', end='')
    help(ajuda)
print('\033[:41m', end='')
linha('ATÈ LOGO!')'''
cores = ('\033[m', #-0 sem cor
         '\033[1:30:41m', #-1 vermelho
         '\033[1:30:43m', #-2 amarelo
         '\033[1:30:44m', #-3 azul claro
         '\033[1:30:47m' #-4 cinza
        )

def titulo(msg, cor=0):
    print(f'{cores[cor]}~' * (len(msg) + 4))
    print(f'  {msg}')
    print(f'~' * (len(msg) + 4))

while True:
    titulo('Sistema de ajuda PyHelp', 2)
    ajuda = str(input(f'{cores[0]}Biblioteca ou Função: ')).lower()
    if ajuda.upper() in 'FIM':
        break
    else:
        titulo(f'Acessando o Manual do comando "{ajuda}"', 3)
        print(f'{cores[4]}', end='')
        help(ajuda)
titulo('Até logo', 1)