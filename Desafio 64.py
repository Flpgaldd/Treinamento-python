n = t = soma = 0
n = int(input("Digite um numero para somar [999 para parar]: "))
while n != 999:
    soma += n
    t += 1  
    n = int(input("Digite um numero para somar [999 para parar]: "))
print(f"A soma dos numeros foi: {soma}")