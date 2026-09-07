soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        soma = soma + x
        cont = cont + 1
print(f"`A soma dos {cont} valores são {soma}")