from datetime import date
atual = date.today().year
ano = int(input("Digite o ano de nascimento: "))
saldo = atual - ano
if saldo <= 9:
    print(f"Atleta tem {saldo} anos de idade")
    print("CLASSIFICAÇÃO: Mirim")
elif saldo <= 14:
    print(f"Atleta tem {saldo} anos de idade")
    print("CLASSIFICAÇÃO: Infantil")
elif saldo <= 19:
    print(f"Atleta tem {saldo} anos de idade")
    print("CLASSIFICAÇÃO: Junior")
elif saldo <= 25:
    print(f"Atleta tem {saldo} anos de idade")
    print("CLASSIFICAÇÃO: Sênior")
elif saldo > 25:
    print(f"Atleta tem {saldo} anos de idade")
    print("CLASSIFICAÇÃO: Master")
