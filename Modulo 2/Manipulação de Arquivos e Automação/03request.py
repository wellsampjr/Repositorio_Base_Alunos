import requests

from bs4 import BeautifulSoup

#Passo 1:esolher uma url
url ='https://sp.senai.br/unidade/santanadeparnaiba'

#Passo 2: Fazer uma requisição HTTP
resposta = requests.get(url)
if resposta.status_code == 200:

    #Passo 3: Usar o BeautifulSoup para interpretar o conteúdo HTML
    soup = BeautifulSoup(resposta.text, 'html.parser')

    #Passo 4: Encontrar titulo da página
    titulo = soup.title.string #Pega o título da página

    #Passo 5: IMprimir o título da página
    print(f"O titulo da pagina é: {titulo}, o melhor do Brasil")

else:
    print(f"Erro ao acessar a página. Código de status: {resposta.status_code}")