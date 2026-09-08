frase = input("Digite uma frase para ver se é palíndroma: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f"Você digitou {junto} e a forma invertida é {inverso}")
if inverso == junto:
    print("Temos uma palavra palíndroma!")
else:
    print("A palavra não é palíndroma!")
