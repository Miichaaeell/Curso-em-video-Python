import dados
from time import sleep
lista = []
try:
    while True:
        sleep(0.5)
        r = dados.menu()
        if r == 1:
            sleep(0.5)
            dados.pessoas(lista)
        elif r == 2:
            sleep(0.5)
            lista.append(dados.cadastro().copy())
        if r == 3:
            sleep(0.5)
            print('Saindo do Programa, até logo')
            break
except KeyboardInterrupt:
    print('\033[31m\nUsuário encerrou o programa\033[m')

