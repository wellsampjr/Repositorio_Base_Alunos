# cria um programa que simule um sistema de emprestimo para um banco
# o programa solicitado ao usuario o valor desejado para emprestimo e a quantidade de parcela
# desejadas
# com base nas informaçoes fornecidas , o programa calcula o valor das parcelas
# e verifica se o emprestimo 
# pode ser aprovado, considerando as seguintes regras:
# o valor minimo para o emprestimo é R$ 1.000,00
# o valor maximo para emprestimo é R$ 50.000,00
# a quantidade minima de parcelas é 6 e a maxima é 36
# o valor da parcela não pode ultrapassar 30% da renda mensal do cliente 

print("simulador de emprestimo")

# criação de variaveis
valor_emprestimo = float (input("digite o valor desejado para o emprestimo: R$ "))
num_parcelas = int(input("digite a quantidade de parcelas desejadas (6 a 36):"))
renda_mensal = float(input("digite sua renda mensal: R$ "))

valor_parcela = valor_emprestimo / num_parcelas
renda_permitida = renda_mensal * 0.3

if valor_emprestimo < 1000 or valor_emprestimo > 50000:
    resultado = "Emprestimo não aprovado: valor fora dos limites permitidos."

elif num_parcelas < 6 or num_parcelas > 36:
    resultado = "Emprestimo não aprovado: quantidade de parcelas invalida"

elif valor_parcela > renda_permitida:
    resultado = f"Emprestimo naõ aprovado: valor das parcelas excede 30% da renda mensal"
else:
    resultado = f"emprestimo aprovado , valor das parcelas: R$ {valor_parcela: .2F}"

print("NRESULTADO")
print(resultado)