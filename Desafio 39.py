from datetime import date

print("Alistamento militar!")
print("="*20)
print("Regras: Alistamento feito somente com 18 anos")
print("="*20)
atual = date.today().year
ano = int(input("Digite a ano:"))
idade = atual - ano
if ano < 2026 or ano == 2026:
    if idade < 18:
        saldo = 18 - idade
        print("Você ainda não precisa se alistar")
        print(f"Você tem {idade} anos - faltam {saldo} anos - seu alistamento sera em {ano + 18}")
    elif idade > 18:
        saldo = idade - 18
        print("Você já deveria ter se alistado!")
        print(f"Você tem {idade} anos - faz {saldo} anos - seu alistamento foi em {ano + 18}")
    elif idade == 18:
        print("Você tem que se alistar esse ano!")
        print(f"Você tem {idade} anos - e seu ano de alistamento é {atual}")
elif ano > 2026:
    print("Essa pessoa nem nasceu ainda!")