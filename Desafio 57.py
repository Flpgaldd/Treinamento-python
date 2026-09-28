sexo = input("Informe seu sexo (M/F): ").upper()
while sexo not in "MmFf":
    sexo = input("Dados invalidos | Por favor digite novamente (M/F):").upper()
    if sexo == "M":
        print("Sexo masculino registrado com sucesso!")
        confirmar = True
    elif sexo == "F":
        print("Sexo feminino registrado com sucesso!")
        confirmar = True
    else:
        continue
