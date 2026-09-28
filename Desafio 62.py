print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1     
total = 0   
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} >> ", end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Você quer ver mais quantos termos: "))
print(f"Progressão da PA teve seu total de {total}")