dados_temporarios = []
lista_principal = []
leve = pesado = 0
while True:

    dados_temporarios.append(str(input('Nome: ')))
    dados_temporarios.append(float(input('Peso: ')))
    if len(lista_principal) == 0:
       leve = pesado = dados_temporarios[1]
    else:
        if leve > dados_temporarios[1]:
            leve = dados_temporarios[1]
        if pesado < dados_temporarios[1]:
            pesado = dados_temporarios[1]
    lista_principal.append(dados_temporarios[:])
    dados_temporarios.clear()
    resposta = str(input('Deseja continuar?'))
    if resposta in 'Nn':
        break

print(lista_principal)
print(f'O total de pessoas cadastradas é de {len(lista_principal)}')
print(f'O menor peso é {leve}Kg, de ', end='')
for p in lista_principal:
    if p[1] == leve:
        print(f'{p[0]} ', end='')
print()
print(f'O maior peso é {pesado}Kg, de ', end='')
for p in lista_principal:
    if p[1] == pesado:
        print(f'{p[0]} ', end='')
