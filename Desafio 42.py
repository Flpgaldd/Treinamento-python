seg1 = float(input("Digite o primeiro segmento: "))
seg2 = float(input("Digite o segundo segmento: "))
seg3 = float(input("Digite o terceiro segmento: "))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    if seg1 == seg2 == seg3:
        print("Os segmentos acima PODEM formar um triagulo EQUILATERO")
    elif seg1 != seg2 != seg3 != seg1:
        print("Os segmentos acima PODEM formar um triagulo ESCALENO")
    else:
        print("Os segmentos acima PODEM formar um triagulo ISOSCELES")
else:
    print("Os segmentos acima NÃO PODEM formar um triangulo")