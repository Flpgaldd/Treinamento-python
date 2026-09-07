dias = int(input("Quantos dias você utilizou o carro: "))
km = int(input("Quantos km você andou: "))
total = (60 * dias) + (km * 0.15)
print(f"O total a pagar pelo aluguel do carro é: R${total}")