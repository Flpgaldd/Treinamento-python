salario = int(input("Digite o salario do funcionario: R$"))
if salario <= 1250:
    aumento = salario * 0.15 + salario
    print(f"quem ganhava R${salario} agora ganha R${aumento}!")
elif salario > 1250:
    aumento = salario * 0.100 + salario
    print(f"quem ganhava R${salario} agora ganha R${aumento}!")
