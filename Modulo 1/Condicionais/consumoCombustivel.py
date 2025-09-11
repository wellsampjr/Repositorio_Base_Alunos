#switch case
# Solicita os dados do usuário

distanciaPercorridada = float(input("Digite a distância percorrida em km: "))
combustivelGasto = float(input("Digite a quantidade de combústivel gasto em litros: "))

# Calculo do consumo médio 
consumoMedio = distanciaPercorridada / combustivelGasto

# Classifica o consumo usando match-case

match consumoMedio:
    case valor if valor < 8:
        print("Consumo menor que 8km/1 - DESEMPENHO RUIM")
    
    case valor if valor > 12:
        print("Consumo entre 8 e 12 km/1 - DESEMPENHO MÉDIO")
    
    case _ :
        print("Consumo maior ou igual a 12 km/1 - ÓTIMO DESEMPENHO")