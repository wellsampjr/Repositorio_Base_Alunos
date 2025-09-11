import json

# String no formato JSON, usar aspas e valores booleanos com letra minúscula

json_data = '{"nome":"Anna","idade":17,"estudante":true}'

dados_python = json.loads(json_data)

print(dados_python['nome'])
print(dados_python['idade'])
print(dados_python['estudante'])
