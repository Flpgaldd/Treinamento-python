import math

co = float(input("Digite o cateto oposto do triangulo: "))
ca = float(input("Digite o cateto adjacente do triangulo: "))
h = math.hypot(co,ca)
print(f"A hipotenusa de CO:{co} e CA:{ca} é {h:.2f}")