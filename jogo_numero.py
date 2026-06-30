# nesse jogo o sitema ira sorteia um numero
# jogador deverar acertar esse numero secreto
#ele tem 5 vidas ante gameover
#precisamos  importar a funcionalidade de sorteio
import random


# dentro do random que  é pacote  de sorteio 
#radint é uma funçao que escolhemos numero
#minimp e maximo para sorteio 
numero_secreto = random.randint(1,100)
ganhou= False
vida=5
# o loop continua enquanto:ainda nao ganhou ou ainda morreu
while ganhou == False and vidas > 0:
    jogada = int (int("sua joaga:"))
    # se os numero forem iguais  vence
    if jogada== numero_secreto:
     ganhou =True
else:
    #errou
    print("voce errou")
    vida=vida-1
    if jogada > numero_secreto:
        print("o seu numero esya acima do secreto") 
    else:
        print("o seu numero esta abaixo secreto")

if vidas > 0:
   print("parabens voce acertou ")
   print("o numero secreto:",numero_secreto)
else:
   print("game over")
   print("o numero secreto:",numero_secreto)             
