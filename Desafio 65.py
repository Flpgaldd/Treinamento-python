r = "S"
soma = cont = media = maior = menor = 0
while r in "Ss":
    n = int(input("Digite um numero: "))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor: 
            menor = n
    r = input("Quer continuar? [S/N] ").upper().strip()[0]
media = soma / cont
print(f"Você digitou {cont} numeros e a média deles é: {media}")
print(f"O maior numero foi {maior} e o menor numero foi {menor}")

    