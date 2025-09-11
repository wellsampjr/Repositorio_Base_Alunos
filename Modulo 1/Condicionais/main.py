print("Revisão for")

#for executa um bloca varias vezes

frutas = ["Maçã", "Banana", "Abacate", "Caju", "Melancia", "Morango"]


for fruta in frutas:
    print(f"Eu gosto de {fruta}")

carros = ["Fit", "Polo", "Bmw", "Punto", "Civic", "Jetta"]

for carro in carros:
    print(f"Eu vou comprar um {carro}")

#while executa um bloco 'enquanto'(while uma condição for verdadeira)

contador = 1
while contador <=5:
    print(f"Contador: {contador}")
    contador = contador + 1

print("Sai o while... ufa!!")

#Crie um programa que peça a senha do cliente. A senha precisa ser "senha135"
#Se a senha estiver correta, imprima que esta ok. caso contrario informe tbm.


senhaCorreta = "senha135"
tentativas = 0
MaxTentativas = 3

while tentativas < MaxTentativas:
    senha = input("Digite sua senha: ")

    if senha == senhaCorreta:
        print("Senha correta")
        break

    else:
        tentativas += 1 
        print(f"Senha incorreta. Tentativa {tentativas} de {MaxTentativas}.")

if tentativas == MaxTentativas:
    print("Limite de tentativas excedido") 





    


