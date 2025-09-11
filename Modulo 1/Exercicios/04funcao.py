# Crie uma funcao que inverta a ordem de um texto 

#Crie uma variavel e receba um texto 

texto = input("Digite uma palavra: ")

def inverterTexto(texto):
    return texto[::-1]

print(inverterTexto(texto))
