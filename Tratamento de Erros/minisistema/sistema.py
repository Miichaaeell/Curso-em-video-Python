from biblioteca.interface import *
from biblioteca.arquivo import *
from time import sleep
try:
    arquivo = str(input('Qual arquivo deseja abrir ou criar? '))
    if not existe(arquivo):
        criar(arquivo)
    while True:
        res = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
        if res == 1:
            print('Carregando...')
            sleep(1)
            cabeçalho('Pessoas cadastradas')
            ler(arquivo)
        elif res == 2:
            sleep(1)
            cabeçalho('Cadastrar nova pessoa')
            cadastro(arquivo)
        else:
            cabeçalho('Saindo do Programa')
            sleep(1)
            break
        sleep(1.5)
except KeyboardInterrupt:
    print('\n\033[31mUsuario encerrou o programa\033[m')