# Crie um jogo de adivinhação de numeros 

import random

def jogar_adivinhacao():
    print("**********************************")
    print("*Bem-vindo ao jogo da adivinhação*")
    print("**********************************")

    numero_secreto = random.randint(1,100) # Melhor usar randint para incluir 100
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    while True:
        try:
            nivel = int(input("Defina o nível: "))
            if nivel in [1, 2, 3]:
                break
            else:
                print("Escolha um nível válido: (1), (2) ou (3).")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    if nivel == 1:
        total_tentativas = 20
    elif nivel ==2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1,total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}")
        
        while True:
            try:
                chute = int(input("Digite um número entre 1 e 100:"))
                if 1 <= chute <= 100:
                    break
                else:
                    print("Número fora do intervalo! Digite um número entre 1 e 100")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

        print(f"Você digitou: {chute}")

        if chute == numero_secreto:
            print(f"Parabéns! Você acertou e fez {pontos} pontos!")
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O número que você chutou é maior que o número secreto.\n")
            else:
                 print("Você errou! O número que você chutou é menor que o número secreto.\n")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = max(0, pontos - pontos_perdidos) #Garante que não sejam negativos 

    print(f"O número secreto era {numero_secreto}. Fim do jogo!")

if __name__ ==  "__main__":
    jogar_adivinhacao()
