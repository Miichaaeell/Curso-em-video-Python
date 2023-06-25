def existe(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar(aqruivo):
    try:
        a = open(aqruivo, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro ao criar o arquivo!\033[m')
    else:
        print('\033[31mArquivo criado com sucesso!\033[m')


def ler(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('\033[31mErro ao abrir o arquivo!\033[m')
    else:
        dado = a.readlines()
        for p in dado:
            print(f'\033[34m{p.split()[0]:<30}\033[m \033[36m{p.split()[1]:>3} anos\033[m')
    finally:
        a.close()


def cadastro(arquivo):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'\033[31mErro ao abrir o Arquivo!\033[m')
    else:
        while True:
            Nome = str(input('\033[37mNome: \033[m')).strip()
            if Nome.isnumeric() or Nome == '':
                print(f'\033[31mErro! informe os dados corretamente\033[m')
            else:
                break
        while True:
            Idade = str(input('\033[37mIdade: \033[m')).strip()
            if not Idade.isnumeric():
                print('\033[31mErro! informe os dados corretamente\033[m')
            else:
                break
        try:
            a.write(f'{Nome} {Idade}\n')
        except:
            print(f'\033[31mErro ao salvar dados!\033[m')
        else:
            print(f'\033[32m{Nome} Cadastrado com Sucesso\033[m')
        finally:
            a.close()
