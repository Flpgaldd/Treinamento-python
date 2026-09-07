primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(f"{c}", end= ' > ')
print("Acabou")