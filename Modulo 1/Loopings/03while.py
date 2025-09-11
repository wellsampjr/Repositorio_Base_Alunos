#Crie um programa que calcule o fatorial de um numero

n = int(input("Digite um número para saber o fatorial: "))
resultado = 1 
f = 1

while f <= n:
    resultado *= f
    f += 1 
    print(f"O fatorial do {n} é: , {resultado}")