dados = {}
gols = []
dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou?'))
for c in range(0, partidas):
   gols.append(int(input(f'Quantos gols na partida {c+1}?')))
dados['Gols'] = gols
dados['Total'] = sum(gols)
print('=-'*30)
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*30)
print(f'O jogar {dados["Nome"]} jogou {partidas} partidas.')
#for c in range(0, partidas):
#    print(f'  => Na partida {c+1}, fez {dados["Gols"][c]} gols.')
for i, v in enumerate(dados['Gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'  => Foi um total de {dados["Total"]} gols')