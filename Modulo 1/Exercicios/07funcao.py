#Crie um programa que calcule a quantidade de bebidas e de carne para a organização de um churrasco

def calcularBebidas(convidados, consumoPorPessoaMl=800,VolumeGarrafaLitros=2.25):
    totalMl = convidados * consumoPorPessoaMl
    totalLitros = totalMl/1000

    garrafas = int(totalLitros//VolumeGarrafaLitros)
    if totalLitros %VolumeGarrafaLitros > 0:
        garrafas += 1
    return totalLitros, garrafas

def calcularCarne(convidados, consumoPorPessoaGramas=400):
    toltalGramas = convidados * consumoPorPessoaGramas  #calcula o total de carne em gramas
    totalKg = toltalGramas / 1000  #conversão de gramas para kg
    return totalKg

convidados = int(input("Digite o número de convidados: "))


#Cálculo 
litros, garrafas = calcularBebidas(convidados)
carneKg = calcularCarne(convidados)

#Resultado
print("n\=== Quantidade Total para o Churrasco ===")
print(f"Refrigerante necessário: {litros:.2f}")
print(f"Garrafas de 2,25L: {garrafas} unidades")
print(f"Carne nescessaria: {carneKg} kg")