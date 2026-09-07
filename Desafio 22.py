if tipo == tipos[0]:
    tipo = "Carro"
    print("===== Carro selecionado =====")
    tipos.append(tipo)
    print(tipos)
elif tipo == "2":
    tipo = "Motocicleta"
    print("===== Motocicleta selecionada =====")
    tipos.append(tipo)
    print(tipos)
elif tipo == "3":
    tipo = "Camionete"
    print("===== Camionete selecionada =====")
    tipos.append(tipo)
    print(tipos)
else:
    print("Valor invalido")