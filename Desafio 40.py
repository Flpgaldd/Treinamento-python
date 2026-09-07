nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Quem tirou {nota1}, {nota2}, {nota3}, tem {media:.1f} de média!")
if media < 5.0:
    print("Você foi reprovado!")
elif media >= 5.0 and media <= 6.9:
    print("Você está de recuperação!")
elif media >= 7.0:
    print("Parabéns!!! você passou!!!")