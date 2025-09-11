#Crie um codigo que faça a coversao de moeda do real para o dolar e vice-versa

#Etapas 
#1) criar uma variavel chamada cotacao
#2) solicitar o usuario a opção de conversao desejada 
#3) apresentar o resultado da conversao de moeda 
#4) perguntar se ele deseja continuar a conversão

letra = "s"
cotacao = 6

while letra == "s":
    
    #escolha qual cotaçao gostaria de fazer 
    print("\nEscolha a opção de conversão:")
    print("1 - Real para Dólar")
    print("2 - Dólar para Real")
    opcao = input("Digite sua opção (1 ou 2): ")

    #cotacao do real para o dolar
    if opcao == "1":
        valor = float(input("Digite o valor em Reais: R$ "))
        convertido = valor / cotacao
        print(f"Valor em Dólares: US$ {convertido:.2f}")

    #cotacao do dolar para o real 
    elif opcao == "2":
        valor = float(input("Digite o valor em Dólares: US$ "))
        convertido = valor * cotacao
        print(f"Valor em Reais: R$ {convertido:.2f}")

    else:
        print("Opção inválida. Tente novamente.")

    letra = input("Deseja continuar ? (s/n): ")