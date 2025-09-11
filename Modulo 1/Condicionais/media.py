# Crie um um programa que solicite a nota de um aluno e informe o conceito recebido.
# Conceito => A = Excelente(nota igual ou maior que  9), 
# B = Muito bom (nota igual ou maior que 8)
# C = Bom(nota igual ou maior que 7), 
# D = Regular(nota igual ou maior que 6)
# E = Insuficiente(nota menor que 6)

nota= float(input("Digite a nota do aluno: "))

if nota >= 9:
    print("Conceito A - Excelente")
elif nota >= 8: 
    print("Conceito B - Muito Bom")
elif nota >= 7:
    print("Conceito C - bom")
elif nota >= 6:
    print("Conceito D - Regular")
else:
    print("Conceito E - Insuficiente")