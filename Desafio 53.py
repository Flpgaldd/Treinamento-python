frase = input("Digite uma frase para ver se é palíndroma: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
invertido = junto[::-1]
print(f"Você digitou {junto} e a forma invertida é {invertido}")
if invertido == junto:
    print("Temos uma palavra palíndroma!")
else:
    print("A palavra não é palíndroma!")
