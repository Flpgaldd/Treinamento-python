cont = 0
soma = 0
while True:
    n = int(input("Digite um numero, para parar o looping digite [999]: "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"A soma dos {cont} valores é {soma}")
