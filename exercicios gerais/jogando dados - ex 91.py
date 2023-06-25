from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = {}
for c in range(0,4):
    jogadores[f'Jogador {c + 1}'] = randint(1, 6)
print(f'{"--->Valores Sorteados<---":^30}')
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print(f'{"==Ranking dos Jogadores==":^30}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#for c in range(0,4):
#    print(f'{c+1}º Lugar: {ranking[c][0]} com {ranking[c][1]}')
for i, v in enumerate(ranking):
    print(f'   {i + 1}ª Lugar: {v[0]} com {v[1]}')