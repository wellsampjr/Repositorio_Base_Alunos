print("Sistema de Classificação de Idade")
print("*"*60)

#Receba a idade do usuário
idade = int(input("Digite sua idade: "))

#Verificar inicial do usuário
if idade <0:
    print("ERRO: idade não pode ser negativa")
else:
    #Condicionais aninhadas para classificar a idade
    if idade < 12 :
        print("Você é uma criança.")

        #Condicionais aninhadas para detalhes sobre crianças
        if idade <=5:
            print("Primeira infância.")
        else:
            print("Pré adolecente.")
    elif idade < 18:
        print("Você é um adolecente.")
        if idade < 15:
            print("Adolecência inicial.")
        else:
            print("Adolecência tardia.")
    elif idade < 60:
        print("Você é um adulto.")
        if idade < 30:
            print("Aduto Jovem.")
        elif idade < 45:
            print("Adulto.")
        else:
            print("Adulto Maduro.")
    else:
        print("Voce é idoso.")
        if idade < 75:
            print("Terceira idade.")
        else:
            print("Quarta idade.")

print("*"*60)



