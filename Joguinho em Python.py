import os
import random
import sys
import time


ouro = { "x": random.randint(0, 9), "y": random.randint(0, 4) }
player = { "nome": "Jogador 1", "x": 0, "y": 0 }


def andar(direcao):
    if direcao == 'w' and player['y'] > 0:
        player['y'] -= 1
    elif direcao == 'a' and player['x'] > 0:
        player['x'] -= 1
    elif direcao == 's' and player['y'] < 4:
        player['y'] += 1
    elif direcao == 'd' and player['x'] < 9:
        player['x'] += 1
x = 0
y = 0


def jogo():
    os.system('cls')
    print('------------------------------------')


    for y in range(5):
        print('\n')
        for x in range(10):
            if (x == player['x'] and y == player['y']):
                print("🤺", end="  ")
            elif (x == ouro['x'] and y == ouro['y']):
                print('🧑', end="  ")
            else:
                print("🟩", end=" ")


    if (player['x'] == ouro['x'] and player['y'] == ouro['y']):
            print('\n')
            print('Voce venceu. Parabens!!!')
            return sys.exit()
   
    print('\n')




def tiro():
    i = player['x'] + 1
    while i < 10:
        os.system('cls')
        for y in range(5):
            print('\n')
            for x in range(10):
                if (x == player['x'] and y == player['y']):
                    print("🤺", end="  ")
                elif (y == player['y'] and x == i and x != ouro['x']):
                    print('💣', end="  ")
                elif (y == ouro['y'] and i == ouro['x'] and x == ouro['x']):
                    print('💥', end="  ")
                    vivo = -1
                elif (x == ouro['x'] and y == ouro['y']):
                    print('🧑', end="  ")
                else:
                    print("🟩", end=" ")
        i += 1
        time.sleep(0.5)
       
while True:
    jogo()
    direcao = input('Digite o proximo passo: ')
    if (direcao == 'a' or direcao == 'w' or direcao == 's' or direcao == 'd'):
        andar(direcao)
    else:
        tiro()