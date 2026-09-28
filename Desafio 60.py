import math
numero = int(input("Digite o numero para calcular o fatorial: "))
resultado = math.factorial(numero)
c = numero 
while c != 0:
    print(f"{c}", end=" ")
    print("x " if c > 1 else "= ", end="")
    c -= 1
print(f"{resultado}") 