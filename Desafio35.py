print('-=' * 20)
print("Analisador de triangulos")
print("-=" * 20)

seg1 = float(input("Digite o primeiro segmento: "))
seg2 = float(input("Digite o segundo segmento: "))
seg3 = float(input("Digite o terceiro segmento: "))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("\033[0:31:47m Os segmentos acima podem formar um triagulo \033[m")
else:
    print("Os segmentos acima não formam um triangulo")