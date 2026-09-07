import math

angulo = float(input("Digite o angulo: "))
c = math.cos(math.radians(angulo))
s = math.sin(math.radians(angulo))
t = math.tan(math.radians(angulo))
print(f"O angulo de {angulo} tem o cosseno:{c}, o seno de {s} e a tangente de: {t}")
