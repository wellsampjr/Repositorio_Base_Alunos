import requests

cep = input("Digite o CEP (somente numeros): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json() #Convertendo a resposta em JSON
    if 'erro' not in dados:
        logradouro = dados['logradouro']
        bairro = dados['bairro']
        cidade = dados['localidade']
        estado = dados['uf']

        print(f"CEP: {cep}")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

    else:
        print("CEP não encontrado.")

else:
    print(f"Erro na requisição: {resposta.status_code}")
    print(resposta.content)