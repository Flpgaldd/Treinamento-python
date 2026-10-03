print("=" * 30)
print("Simulador de caixa eletronico")
print("=" * 30)
valor = int(input("Digite o valor que você quer retirar do caixa: R$"))
total = valor
ced = 50
totalc = 0
while True:
    if total >= ced:
        total -= ced
        totalc += 1
    else:
        if totalc > 0:
            print(f"O total de {totalc} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalc = 0
        if total == 0:
            break

