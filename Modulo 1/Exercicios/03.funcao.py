#Crie uma funcao que identifique se o numero é par ou impar 

num = int(input("Digite um número: "))

def parImpar(n):

    if num % 2 == 0:
        return "Par" 
    else:
        return "Impar" 

print(parImpar(num)) 