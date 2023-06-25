def leiaint(n):
    válidado = False
    while not válidado:
        validar = str(input(n)).strip()
        if not validar.isnumeric():
            print(f'\033[31m ERRO! \"{validar}\" não é um  número inteiro válido\033[m')
        else:
            válidado = True
            return int(validar)


def linha(param=42):
    print('\033[30m-\033[m'*param)


def cabeçalho(msg):
    linha()
    print(f'\033[35m{msg:^42}\033[m')
    linha()


def menu(opc):
    while True:
        cabeçalho('\033[35mMenu principal\033[m')
        c = 1
        for o in opc:
            print(f'\033[33m{c}\033[m - \033[37m{o}\033[m')
            c += 1
        linha()
        res = leiaint('\033[37mSua Opção: \033[m')
        if res == 0 or res > c - 1:
            print(f'\033[31mErro! O valor informado não faz parte do Menu\033[m')
        else:
            return int(res)
            break
