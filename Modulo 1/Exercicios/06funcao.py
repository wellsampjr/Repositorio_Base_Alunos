#Vamos resolver esse problema em python utilizando função, contudo,
# em vez de valores fixo vamos solicitar ao usuário as informações 


# Uma piscina tem 10m de comprimento, 7m de largura, e 1,80m de profundidade.
# Como estava completamente cheia, dela foram retirados 4 830 litros.
#Quantos litros ainda restam?


# Função para calcular o volume em litros (1 m3 = 1000 litros)
def calcularVolumeCm3(comprimento, largura, profundidade): 
    return comprimento * largura * profundidade


def volumeRestante(volumeTotalLitros, VolumeRetiradoLitros):
    return volumeTotalLitros - VolumeRetiradoLitros


#Solicitar dimenções 
comprimento = float(input("Digite o comprimento em (m): "))
largura = float(input("Digite a largura em (m): "))
profundidade = float(input("Digite a profundidade em (m): "))
VolumeRetiradoLitros = float(input("Digite o qual foi o volume retirado da piscina em (L)? : "))

#Calculo do volume em m3
volumeCm3 = calcularVolumeCm3 (comprimento, largura, profundidade)
volumeTotalLitros = volumeCm3 * 1000

#Volume restante
restante = volumeRestante(volumeTotalLitros, VolumeRetiradoLitros)

print(f"Volume total da piscina: {volumeTotalLitros:.0f} litros.")
print(f"Volume retirado: {VolumeRetiradoLitros:.0f} litros.")
print(f"Volume restante: {restante:.0f} litros.")