import requests
import json
import pyautogui
import time
from bs4 import BeautifulSoup

#1. Url da pagina
url = "https://pt.wikipedia.org/wiki/Python"

#2.Faz a requisição HTTP
response = requests.get(url)
response.encoding = 'utf-8'

#3.Use o BeautifulSoup para parsear o HTML
soup = BeautifulSoup(response.text, 'html.parser')

#4.Extrair titulo e primeiro parágrafo
titulo = soup.title.string
primeiro_paragrafo = soup.find('p').text


#5.Montar um dicionario Python
dados = {
    "titulo": titulo,
    "primeiro_paragrafo": primeiro_paragrafo
}

#6. Converter de python para json
dados_json = json.dumps(dados, indent=4, ensure_ascii=False)

#7.Salvar em arquivo json
with open("python_wikipedia.json", "w", encoding="utf-8") as f:
    f.write(dados_json)

#8. Pyautogui imprime no terminal
print("Abra o terminal e posicione o cursor, a digitacao sera feita em 5 segundos...")
time.sleep(5)
pyautogui.write(dados_json, interval=0.01)