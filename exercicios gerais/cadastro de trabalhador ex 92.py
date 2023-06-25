from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = datetime.now().year - nascimento
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = cadastro['Contratação'] + 35 - nascimento
for k, v in cadastro.items():
    print(f'{k} é {v}')