lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    decisao = str(input('Quer continuar?'))
    if decisao in "Nn":
        break
    while decisao not in "Ss":
        decisao = str(input('Quer continuar?'))
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'{lista}'
      f'{pares}'
      f'{impares}')