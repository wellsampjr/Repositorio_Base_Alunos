#Separar diretorios e arquivos 

import os

caminho = "/home/user/documentos/arquivo.txt"
print(os.path.dirname(caminho))  # Exibe o diretório
print(os.path.basename(caminho))  # arquivo.txt
