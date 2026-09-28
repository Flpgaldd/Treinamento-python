import time
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
opcao = 0
while opcao != 5:
    print('=-' * 15)
    print('''[1] Somar \n
    [2] Multiplicar \n
    [3] Maior \n
    [4] Novos números \n
    [5] Sair do programa''')
    print('=-' * 15)
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        soma = n1 + n2
        print(f"{n1} + {n2} é igual a {soma}")
    elif opcao == "2":
        m = n1 * n2
        print(f"{n1} * {n2} é igual a {m}")
    elif opcao == "3":
        maior = max(n1, n2)
        print(f"O maior numero entre {n1} e {n2} é {maior}")
    elif opcao == "4":
        n1 = int(input("Digite outro valor: "))
        n2 = int(input("Digite mais um valor: "))
    elif opcao == "5":
        print("Finalizando...")
        time.sleep(2)
        break
    else:
        print("Erro! Opção invalida!")
    time.sleep(2)
print("Fim do programa!")