print(5 * '=' + "Loja Felipe" + 5 * '=')
valor = int(input("Qual o valor da compra: R$"))
opcao = int(input("[ 1 ] À vista dinheiro/cheque: \n" \
"[ 2 ] À vista no cartão: \n" \
"[ 3 ] 2x vezes no cartão: \n" \
"[ 4 ] 3x ou mais no cartão: \n"))
if opcao == 1:
    desconto = valor - (valor * 10 / 100) 
    print(f"Sua compra foi de R${valor:.2f} vai custar R${desconto:.2f} no final!")
elif opcao == 2:
    desconto = valor - (valor * 5 / 100) 
    print(f"Sua compra foi de R${valor:.2f} vai custar R${desconto:.2f} no final!")
elif opcao == 3:
    parcela = valor / 2
    print(f" Sua compra de R${valor:.2f} vai ser parcelada em 2x de R${parcela:.2f}, valor final: R${valor:.2f}")
elif opcao == 4:
    juros = valor + (valor * 20 / 100) 
    totaparc = int(input("Quantas parcelas? "))
    parcelas = juros / totaparc
    print(f"Sua compra de R${valor:.2f} sera parcelada em {totaparc}x e tera 20% de juros! Valor das parcelas: R${parcelas:.2f} - Valor final: R${juros:.2f}")
else:
    print("Opção invalida!")