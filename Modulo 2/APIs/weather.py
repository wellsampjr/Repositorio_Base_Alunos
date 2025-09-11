#Criar um codigo que consuma ua api de clima e imforama a temperatura e a descricao do clima em um lugar especifico 

import requests

#01. Definir chave de API e o link da requisição

api_key = "2a1ac38a32354cb7b19133643251408"
cidade = input("Digite o nome da cidade: ").strip()
url = f"http://api.weatherapi.com/v1/current.json"


#02. Parametros da requisição

parametros = {
    "key": api_key,
    "q": cidade,
    "lang": "pt"
}

#03. Fazer a requisição
resposta = requests.get(url, params=parametros)

#04. Verificar se a requisição foi bem sucedida

if resposta.status_code == 200:
    dados= resposta.json() # convertendo a resposta em JSon em um dicionario python
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']

 #05. Apresenta os resultados

    print(f"Temperatura na cidade de {cidade} é {temperatura}°C.")
    print(f"Descricao do clima: {descricao}.")

else:
    print(f"Erro na requisição: {resposta.status_code}")
    print(resposta.content)

