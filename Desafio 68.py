import random
print("=" * 30)
print("Jogo do par e ímpar")
print("=" * 30)
while True:
    bot = random.randint(1, 10)
    n = int(input("Diga um valor: "))
    op = input("Escolha Par [P] ou Ímpar [I]: ").upper().split()[0]
    soma = bot + n
    if soma % 2 == 0:
        if op == "P":
            print(f"Você jogou {n} e o computador {bot} e a soma é {soma} - DEU PAR!")
            print("-=" * 30)
            print("Você ganhou!")
            print("-=" * 30)
            print("Vamos jogar novamente!")
        elif op == "I":
            print(f"Você jogou {n} e o computador {bot} e a soma é {soma} - DEU PAR!")
            print("-=" * 30)
            print("Você perdeu ;(")
            print("-=" * 30)
            break
    else:
        if op == "P":
            print(f"Você jogou {n} e o computador {bot} e a soma é {soma} - DEU iMPAR!")
            print("-=" * 30)
            print("Você perdeu ;(")
            print("-=" * 30)
            break
        elif op == "I":
            print(f"Você jogou {n} e o computador {bot} e a soma é {soma} - DEU IMPAR!")
            print("-=" * 30)
            print("Você ganhou!")
            print("-=" * 30)
            print("Vamos jogar novamente!") 
print("Acabou!")