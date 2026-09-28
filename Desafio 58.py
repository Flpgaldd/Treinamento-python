import random
contador = 0
chute = 0
print("Olá... eu sou seu computador!")
print("Pensei em um numero entre 0 a 10, sera que consegue adivinha?")
numero = random.randint(0, 10)
while chute != numero:
    chute = int(input("Digite o numero: "))
    contador += 1
    if chute == numero:
        print(f"Você acertou! o numero era {numero}")
        print(f"Acertou em {contador} tentativas!")
    elif chute < numero:
        print("Mais... Tente novamente!")
        continue
    elif chute > numero:
        print("Menos... Tente novamente!")