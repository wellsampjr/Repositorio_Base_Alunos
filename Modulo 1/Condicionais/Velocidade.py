#Crie um programa que verifique infracoes de transito: rodizio de velocidade

#pergunte se hoje e rodizio do carro
#pergunte a velocidade do carro
#defina o lomite de velociadade da via 
#verifique as infracoes 



rodizio = input("Hoje é dia de rodizio deste carro? (sim/não): ").strip().lower()
velocidade =int(input("A qual velocidade está seu veiculo: "))

limiteVia = 60


if rodizio == "sim" and velocidade > limiteVia :

    print("Você está dirigindo no seu dia de rodizio e acima da velocidade permitida.\n")
    print("Você está sendo autuado pelas infrações")

elif rodizio =="sim":

    print("Você está dirigindo no seu dia de rodizio e será autuado por isso")

elif velocidade > limiteVia:

    print("Você está dirigindo acima da velocidade permitida e será autuado por isso")

else:
    print("Tudo certo! Você está dentro da lei. Dirija com segurança")