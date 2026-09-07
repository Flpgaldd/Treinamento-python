from random import randint
from time import sleep
print(5 * "=" + "JOKENPO!!!" + 5 * "=")
jogo = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções:
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura""")
jogador = int(input("Qual sua jogada? "))
if jogador < 0 or jogador > 2:
    print("JOGADA INVALIDA!")
else:
    print("JO...")
    sleep(1)
    print("KEN...")
    sleep(1)
    print("PO!!!")
    print(20 * "-=")
    print(f"Jogador jogou: {jogo[jogador]}")
    print(f"Computador jogou: {jogo[computador]}")
    print(20 * "-=")
    if computador == 0:
        if jogador == 0:
            print("EMPATE!")
        elif jogador == 1:
            print("JOGADOR VENCEU!")
        elif jogador == 2:
            print("COMPUTADOR VENCEU!")
        else:
            print("JOGADA INVÁLIDA!")
        
    elif computador == 1:
        if jogador == 0:
            print("COMPUTADOR VENCEU!")
        elif jogador == 1:
            print("EMPATE!")
        elif jogador == 2:
            print("JOGADOR VENCEU!")
        else:
            print("JOGADA INVÁLIDA!")
    elif computador == 2:
        if jogador == 0:
            print("JOGADOR VENCEU!")
        elif jogador == 1:
            print("COMPUTADOR VENCEU!")
        elif jogador == 2:
            print("EMPATE!")
        else:
            print("JOGADA INVÁLIDA!")