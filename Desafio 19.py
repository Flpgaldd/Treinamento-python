import random
nome1 = str(input("Digite o nome de um aluno: "))
nome2 = str(input("Digite o nome de um aluno: "))
nome3 = str(input("Digite o nome de um aluno: "))
nome4 = str(input("Digite o nome de um aluno: "))

n = [nome1, nome2, nome3, nome4]
print(f'O nome sorteado para apagar o quadro foi: {random.choice(n)}!')