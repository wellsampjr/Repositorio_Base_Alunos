#Abrir e ler um arquivo 

arquivo = open("hello.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

