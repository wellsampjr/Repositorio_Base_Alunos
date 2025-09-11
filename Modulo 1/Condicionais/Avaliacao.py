#Coletar as informações do usuario
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))

#Calcular o IMC

imc = peso/(altura**2)
                       
print("_"*50)


#Responder o usuario de acordo com o seu IMC
if imc >= 40.0 :
    print(f"{nome} tenha cuidado com a Saúde")
    print(f"Você está com: Obesidade Grau III (mórbida), tendo um IMC de {imc:.2f}")

elif imc >= 35.0 :
    print(f"{nome} tenha cuidado com a Saúde")
    print(f"Você está com: Obesidade Grau II, tendo um IMC de {imc:.2f} ")

elif imc >= 30.0 :
    print(f"{nome} tenha cuidado com a Saúde")
    print(f"Você está com: Obesidade Grau I, tendo um IMC de {imc:.2f} ")

elif imc >= 25.0 :
    print(f"{nome} está tudo ok")
    print(f"Você está com: Sobrepeso, tendo um IMC de {imc:.2f}")

elif imc >= 18.5 :
    print(f"{nome} está tudo ok")
    print(f"Você está com: Peso normal, tendo um IMC de {imc:.2f}")

else:
    print(f"{nome} tenha cuidado com a Saúde")
    print(f"Você está: Abaixo do peso, tendo um IMC de {imc:.2f}")