'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

Create a program that manages a football player's performance. The program will read the player name
and how many games he played. Then it will read the number of goals scored in each match. In the end, all this
will be saved in a dictionary, including the total goals scored during the championship.
'''
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, total):
    partidas.append(int(input(f'   Quantos gols na partidas {i+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'    => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
