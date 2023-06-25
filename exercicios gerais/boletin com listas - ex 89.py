'''nomes = list()
notas = list()
medias = list()
dados = list()
alunos = list()
n = list()
while True:
    nome = str(input('Nome: '))
    nomes.append(nome)
    alunos.append(nome)
    nota1 = float(input('Nota 1: '))
    n.append(nota1)
    nota2 = float(input('Nota 2: '))
    n.append(nota2)
    notas.append(n[:])
    n.clear()
    medias.append((nota1 + nota2) / 2)
    alunos.append((nota1 + nota2) / 2)
    dados.append(alunos[:])
    alunos.clear()
    decisao = str(input('Deseja continuar? '))
    if decisao in 'Nn':
        break
print('=*'*15)
print(f'No.   NOME             MÉDIA')
print('--'*15)
for i, p in enumerate(dados):
    print(f'{i} {p[0]:<15} {p[1]:>10}')
print('--'*15)
while True:
    indice = int(input('Mostrar notas de qual aluno? (99 para sair) '))
    if indice == 99:
        break
    print(f'Notas de {nomes[indice]} são {notas[indice]}')'''

dados = list()
while True:
    nome = str(input('nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    decisao = str(input('Deseja Continuar?'))
    if decisao in 'Nn':
        break
print('='*30)
print(f'{"No.":<4}{"NOME":<20}{"MÉDIA":>8}')
print('='*30)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<20}{a[2]:>8.1f}')
print('='*30)
while True:
    deta = int(input('De qual aluno deseja ver as notas? (99 para sair)'))
    if deta == 99:
        print('FINALIZANDO')
        break
    if deta <=len(dados) -1:
        print(f'As notas de {dados[deta][0]} são {dados[deta][1]}')
        print()
print('<<< VOLTE SEMPRE >>>')
