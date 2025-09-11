#Crie um programa que pergunte ao cliente se é sua primeira compra
#depois pergunte o valor total da compra
#Se for a primeira compra do usuario e esta for maior que 500 reais,
#informe que ele ganhou um brinde e imprima uma mensagen de boas vindas 
#caso contrário imprima uma mensagen de agradecimento

primeiraCompra = input("Essa é sua primeira compra conosco ? (sim/não): ").strip().lower()
valorCompra  = float(input("Informe o valor total da compra: R$ "))

if primeiraCompra == "sim" and valorCompra > 500:
    print("Parabéns! Seja bem vindo a nossa loja, você ganhou um brinde de boas vindas ")

else:
    print("Agradecemos pela preferencia! Volte sempre")