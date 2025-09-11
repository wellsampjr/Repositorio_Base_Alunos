def calcular_preco_final(valor_compra):
    if valor_compra <= 100:
        desconto = 0
    elif valor_compra <= 500:
        desconto = 0.05
    else:
        desconto = 0.10

    valor_desconto = valor_compra * desconto
    valor_final = valor_compra - valor_desconto

    return valor_final, valor_desconto, desconto * 100  # Retorna também o valor do desconto e a porcentagem


# Programa principal
print("=== Calculadora de Desconto ===")

valor = float(input("Digite o valor total da compra: R$ "))

valor_final, valor_desconto, porcentagem = calcular_preco_final(valor)

print(f"\nDesconto aplicado: {porcentagem:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")

