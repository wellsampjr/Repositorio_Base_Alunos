# Exibir o menu da pizzaria 

print("Menu da Pizzaria Tom Jobim:")
print("1- Margherita")
print("2- Calabresa")
print("3- Portuguesa")
print("4- Quatro Quejos")
print("5- Frango com Catupiry")
print("6- SAIR")

while True:
    try:
        # Solicitar o código do sabor
        codigoPizza = int(input("Digite o código da pizza desejada: "))

        #usar match-case para mostrar os sabores e preços
        match codigoPizza:
           
            case 1:
                print("Pizza Margherita - Preço R$ 60,00 ")
            case 2:
                print("Pizza Calabresa - Preço R$ 55,00 ")
            case 3:
                print("Pizza Portuguesa - Preço R$ 70,00 ")
            case 4:
                print("Pizza Quatro Queijos - Preço R$ 59,90 ")
            case 5:
                print("Pizza Frango com Catupiry - Preço R$ 73,00 ")
            case 6:
                print("SAINDO DO MENU")
                break # Sai do loop
            case _:
                print("Código inválido. Por favor, tente novamente")
                
    except ValueError:
         print("Entrada inválida. Digite um número inteiro.")

