nome = input("Qual seu nome? :")
idade = int(input("Qual a sua idade? :"))
possuiCarteira = input("Possui carteira de motorista? \n (1-sim/ 2-não)")

if idade >= 18:
    if possuiCarteira == "1":
        print("Pode dirigir!")
    
    else:
        print("Não pode dirigir pois não possui carteira de motorista")

else:
    print("Não pode dirigir por ser menor de idade")