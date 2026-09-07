peso = float(input("Qual seu peso? (Kg): "))
altura = float(input("Qual sua altura: "))
imc = peso / altura ** 2
print(f"Seu IMC é {imc:.1f}")
if imc < 18.5:
    print("Nivel de IMC: MAGRO")
elif 18.5 <= imc <= 24.9:
    print("Nivel de IMC: NORMAL")
elif 25.0 <= imc <= 29.9:
    print("Nivel de IMC: SOBRE PESO")
elif 30.0 <= imc <= 39.9:
    print("Nivel de IMC: OBESIDADE")
elif imc >= 40.0:
    print("Nivel de IMC: OBESIDADE GRAVE CUIDADO!")