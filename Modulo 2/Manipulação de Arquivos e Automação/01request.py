import requests

res = requests.get('https://www.wikipedia.org/')
print(res.status_code)  #Verifica o status da requisição
print(res.text[:500]) #imprimir os primeiros 500 caracteres da resposta
