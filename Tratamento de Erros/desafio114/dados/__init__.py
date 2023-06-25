def menu():
    resposta = False
    while not resposta:
        print('-'*30)
        print(f'\033[34m{"MENU PRINCIPAL":^30}\033[m')
        print('-'*30)
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova Pessoa')
        print('3 - Sair do Sistema')
        print('-'*30)
        pergunta = str(input('Sua Opção: ')).strip()
        if not pergunta.isnumeric():
            print('\033[31mERRO! O valor informado não é válido, tente novamente\033[m')
        elif int(pergunta) == 0 or int(pergunta) > 4:
            print('\033[31mERRO! O valor informado não faz parte do Menu, tente novamente\033[m')
        else:
            resposta = True
            return int(pergunta)


def cadastro():
    lista = {}
    print('-'*30)
    print(f'{"NOVO CADASTRO":^30}')
    print('-'*30)
    while True:
        lista['Nome'] = str(input('Nome: ')).strip()
        if lista['Nome'].isnumeric() or lista['Nome'] == '':
            print(f'\033[31mErro! informe os dados corretamente\033[m')
        else:
            break
    while True:
        lista['Idade'] = str(input('Idade: ')).strip()
        if not lista['Idade'].isnumeric():
            print('\033[31mErro! informe os dados corretamente\033[m')
        else:
            break

    print('Cadastrado com Sucesso')
    return lista


def pessoas(lista):
    print('-'*30)
    print(f'{"Pessoas Cadastradas":^30}')
    print('-'*30)
    for p in lista:
        print(f'{p["Nome"]:<22}{p["Idade"]:>3} anos')
    print(f'Total de {len(lista)} pessoa(s) cadastrada(s)')