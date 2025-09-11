import json 

pessoa = '{"nome":"Carlos","idade":45,"estudante":false}'

json_string = json.dumps(pessoa)
print(json_string)
 