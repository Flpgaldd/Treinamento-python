from datetime import date
atual = date.today().year
totalma = 0
totalme = 0
for pess in range(1, 8):
    nasc = int(input(f"Digite o ano de nascimento da {pess}° pessoa: "))
    idade = atual - nasc
    print(f"A pessoa tem: {idade} anos de idade!")
    if idade >= 18:
        totalma += 1
    else:
        totalme += 1
print(f"São {totalma} pessoas maiores de idade!")
print(f"São {totalme} pessoas menores de idade!")