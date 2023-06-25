def ficha(jogador='<Desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) na temporada')


nome = str(input('Digite o nome do jogador: '))
g = str(input(f'Quantos gols {nome} fez na temporada? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)