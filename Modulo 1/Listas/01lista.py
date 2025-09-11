numeros = [1,2,3,4,5] #sitaxe para construir uma lista => nome = [] 

print(type(numeros)) # a funcao type informa o tipo da variave 

print(numeros[0]) # função para buscar um elemento especifico da lista 

print(numeros[-1]) #para conhecer o ultimo elemento de uma lista 

numeros[2] = 10 #substituir um elemento que estava no indice 2
print(numeros)

numeros.append(6) # adiciona um elemento no FINAL da lista 
print(numeros)

numeros.remove(4) #remove um objeto especifico de uma lista 
print(numeros)