cadastro = dict()
dados = list()
media = list()
mulheres = list()
soma =  0
while True:
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Sexo'] = str(input('Sexo: [M/F]'))
    if cadastro['Sexo'] not in 'MmFf':
        print('Erro! Digite apenas M ou F.')
        cadastro['Sexo'] = str(input('Sexo: [M/F]'))
    cadastro['Idade'] = int(input('Idade:'))
    #media.append(cadastro['Idade'])
    soma += cadastro['Idade']
    if cadastro['Sexo'] in 'Ff':
        mulheres.append(cadastro.copy())
    dados.append(cadastro.copy())
    resp = str(input('Quer continuar? [S/N]'))
    if resp not in 'SsNn':
        print('Erro! Digite apenas S ou N.')
        resp = str(input('Quer Continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo temos {len(dados)} pessoas cadastradas')
#print(f'A média de idade é {sum(media) / len(media):.0f}')
print(f'A média de idade é {soma / len(dados)}')
print('As Mulheres cadastradas foram ', end='')
#for i, p in enumerate(mulheres):
#    print(f'{p["Nome"]} ', end='')
for p in dados:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end=' ')
print()
print('Lista de pessoas que estão acima da média:')
#for i, p in enumerate(dados):
#    if p['Idade'] >= sum(media) / len(media):
#        print(f'  ->Nome: {p["Nome"]}, Sexo: {p["Sexo"]}, Idade: {p["Idade"]} ')
for p in dados:
    if p['Idade'] >= (soma / len(dados)):
        #print(f'  -> Nome: {p["Nome"]}, Sexo: {p["Sexo"]}, Idade: {p["Idade"]}')
        for k, v in p.items():
            if k == 'Nome':
                print(f' -> {k} = {v} ', end=' ')
            else:
                print(f' {k} = {v} ', end=' ')
        print()