# Crie um programa que consulte os preços dos produtos 
# e sai do programa quando solicitado pelo usuário

print("Códigos de produtos: ")
print("1 - Gin")
print("2 - Gelo")
print("3 - Whisky")
print("4 - Copo")
print("5 - Água")
print("0 - Sair")

while True:
    try:
        #Solicitar o código do produto ao usúário
        codigo = int(input("Digite o código do produto: "))

        # Usar match-case para mostrar o preço com base no código
        match codigo:
            case 1:
                print("Produto: Gin - Preço: R$ 10,00")
            case 2:
                print("Produto: Gelo - Preço: R$ 5,00")
            case 3:
                print("Produto: Whisky - Preço: R$ 45,00")
            case 4: 
                print("Produto: Copo - Preço: R$ 2,50")
            case 5: 
                print("Produto: Água - Preço: R$ 5,00")
            case 0 :
                print("Saindo do programa")
                break # Sai do loop e encerra o programa 
            case _:
                print("Código do produto inválido. Por favor, tente novamente.")

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


