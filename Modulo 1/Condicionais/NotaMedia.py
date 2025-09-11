nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
notaFinal = ((nota1+nota2+nota3)/3)

print(f"Sua nota final é de {notaFinal}")

if notaFinal == 10:
    print("Parabens, voce tirou nota maxima")

elif notaFinal <5:
    print("Reprovado")

else:
    print("Aprovado")













