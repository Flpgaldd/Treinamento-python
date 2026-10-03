soma = produto1000 = barato = cont = 0
print("=" * 30)
print("Valores e produtos")
print("=" * 30)
while True:
    produto = input("Produto: ")
    valor = int(input("Preço: R$"))
    cont += 1
    soma += valor
    if valor > 1000:
        produto1000 += 1
    if cont == 1 or valor < barato:
        barato = valor
        nome = produto  
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? S/N:").upper().strip()[0]
    if continuar == "N":
        break
print(f"Total do valor da compra: R${soma},00")
print(f"Tem {produto1000} produtos com o valor maior que R$1000,00")
print(f"O produto mais barato foi {nome} com o valor R${barato},00")
    
