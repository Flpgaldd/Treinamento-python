print("=" * 30)
print("Cadastre uma pessoa!")
print("=" * 30)
conti = 0
conth = 0
contm = 0
while True: 
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper().split()[0]
    if idade >= 18:
            conti += 1
    if idade < 20 and sexo == "F":
         contm += 1
    if sexo == "M":
         conth += 1
    continuar = input("Quer continuar? S/N: ").upper().split()[0]
    if continuar == "N":
        break
    elif continuar == "S":
        continue
    else:
         print("Resposta invalida!")
print(f"Total de pessoas com mais de 18 anos: {conti}")
print(f"Total de homems cadastrados: {conth}")
print(f"Total de mulheres com menos de 20 anos: {contm}")
print("Fim!")