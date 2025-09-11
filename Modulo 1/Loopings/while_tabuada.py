print("Tabuada de todos os numers de 1 a 10 utilizando o while")

num = 1
while num <= 10 :
    print(f"Tabuada do {num}")
    contador = 1
    while contador <= 10:
       resultado = num*contador
       print(f"{num}x{contador} = {resultado}")
       contador += 1 
    num += 1


