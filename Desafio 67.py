num = 0
num2 = 0
while True:
    n = int(input("Quer ver a tabuada de que valor? "))
    num = n
    if num > 0:
        print("=" * 20)
        num2 = 0
        cont = 0
        while cont < 10:
            num2 += 1
            result = num * num2
            print(f"{num} x {num2} = {result}") 
            cont += 1
        print("=" * 20)
    else:
        break
print("Acabou!")