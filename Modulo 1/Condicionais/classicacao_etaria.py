#Crie um programa de classificação indicativa para eventos culturais

# L = livre para todos os públicos
# 10 = não recomendado para menores de 10 anos
# 12 = não recomendado para menores de 12 anos
# 14 = não recomendado para menores de 14 anos
# 16 = não recomendado para menores de 16 anos
# 18 = não recomendado para menores de 18 anos

idade= int(input("Qual a sua idade?"))

if idade < 10:
    print("Você apesnas pode assistir conteúdos com classificação livre.")
elif idade >10 and idade <=12:
    print("Você pode assistir conteúdos com classisficação para menores de 12 anos.")
elif idade >12 and idade <=14:
    print("Você pode assistir conteúdos com classisficação para menores de 14 anos.")
elif idade >14 and idade <=16:
    print("Você pode assistir conteúdos com classisficação para menores de 16 anos.")
elif idade >16 and idade <=18:
    print("Você pode assistir conteúdos com classisficação para menores de 18 anos.")
else:
    print("Você pode assistir a conteúdos com qualquer classificação etária.")