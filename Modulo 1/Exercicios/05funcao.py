#Crie um programa que calcule o volume de um águario atraves de uma funcao e apresente o resultado

def calcularVolumeCm3(altura, profundidade, largura):
    #Calculo d volume do recipiente 
    return altura * profundidade * largura


#Entradas do usúario 
altura = float(input("Digite a altura em (cm): "))
largura = float(input("Digite a largura em (cm): "))
profunidade = float(input("Digite a profundidade em (cm): "))

#Calculo do volume
volumeCm3 = calcularVolumeCm3(altura, largura, profunidade)

print(f"\n As medidas do áquario são: ")
print(f"Altura: {altura} cm")
print(f"Largura: {largura} cm")
print(f"Profundidade: {profunidade} cm")
print(f"Protanto, seu volume é de {volumeCm3} cm³ ({volumeCm3/1000:.2f} litros )")
