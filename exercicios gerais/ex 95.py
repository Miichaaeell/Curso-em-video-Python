jogador = {}
gol = []
InfoJogadores = []
while True:
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogador['TotPartidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for g in range(0, jogador['TotPartidas']):
        gol.append(int(input(f'Quantos gols na partida {g+1}: ')))
    jogador['Gols'] = gol.copy()
    gol.clear()
    InfoJogadores.append(jogador.copy())
    continuar = str(input('Quer continuar ? [S/N] ')).upper()
    if continuar == 'N':
        break
print('-='*30)
print(f'{"Cod":<} {"Nome":^15} {"Gols":<20} {"Total":>2} ')
print('-'*50)
for i, j in enumerate(InfoJogadores):
    print(f'{i+1:<} {j["Nome"]:^15} {str(j["Gols"]):<20} {sum(j["Gols"]):>2}')
print('-'*50)
while True:
    DetalheJogador = int(input('Mostrar dados de qual jogador? (99 encerra o programa)'))
    if DetalheJogador == 99:
        break
    if DetalheJogador > len(InfoJogadores) or DetalheJogador == 0:
        print(f'Não existe o jogador {DetalheJogador}')
    else:
        print(f' --Levantamento do Jogador {InfoJogadores[DetalheJogador -1]["Nome"]}')
        for p, g in enumerate(InfoJogadores[DetalheJogador -1]['Gols']):
            print(f'No jogo {p+1} fez {g} Gols ')
    print('-'*50)
print('<<< Volte Sempre >>>')
