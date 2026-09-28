nomes = []
idades = []
sexos = []
contador = 0
for i in range(1, 5):
    print(f"==== {i}° pessoa ====")
    nome = input("Digite o nome da pessoa: ").capitalize()
    nomes.append(nome)
    idade = int(input("Digite a idade da pessoa: "))
    idades.append(idade)
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
    sexos.append(sexo)
    if i == 1:
            nomemaior = nome
            maior = idade
    else:
        if idade > maior and sexo == "M":
            nomemaior = nome
            maior = idade
    if sexo == "F" and idade <= 20:
            contador += 1
calculo= sum(idades) / 4   
print(f"A média de idade das pessoas é {calculo}")
print(f"O nome do homem com a maior idade registrada é: {nomemaior}")
print(f"Ao todo são {contador} mulheres com menos de 20 anos")