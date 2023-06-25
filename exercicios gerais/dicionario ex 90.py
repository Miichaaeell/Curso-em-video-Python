dados = {}
dados['nome'] = str(input('Nome: '))
dados['Média'] = float(input(f'Média de {dados["nome"]}: '))
print('=-'*20)
if dados['Média'] <=4.99:
    dados['Situação'] = 'Reprovado'
elif dados['Média'] > 5 and dados['Média'] < 7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Aprovado'
#print(f'-O nome é {dados["nome"]}')
#print(f'-A média é {dados["Média"]}')
#print(f'- A Situação é: {dados["Situação"]}')
for k, v in dados.items():
    print(f' -{k} é: {v}')