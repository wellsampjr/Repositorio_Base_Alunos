# Instalamos no termina o flask com pip install flask
# Importamos a biblioteca flask

from flask import Flask,make_response,jsonify,request
from bd_livros import livros

# Bibliotecas 
# jsonify - converte listas e dicionários em json
# make_response - cria respostas http completa e permite personalizar cabecalhos e código de status
# request - requisições http 

# Instalamos o flask,m ou seja, tornamos a classe (molde) Flask em um objeto (instância)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# GET - lista todos os livros

@app.route('/livros', methods=['GET'])
def get_livros():
    return make_response(jsonify(
        mesagem = "Lista de livros",
        dados = livros

    ))

# GET - Buscar um livro pelo id
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return make_response(jsonify(
                mesagem = f"Livro id: {id} encontrado",
                dados = livro
            ))
    return make_response(jsonify(
        mesagem = f"Livro id: {id} não encontrado"
    ),404
    )

# POST - Cadastrar um novo livro
@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return make_response(jsonify(
        mesagem = "Livro cadastrado com sucesso",
        dados = novo_livro
    ),201)


#PUT - Atualizar um livro
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    for livro in livros:
        if livro.get('id') == id:   
         novo_livro = request.get_json()
         livro.update(novo_livro)
         return make_response(jsonify(
             mesagem = f"Livro id: {id} atualizado com sucesso",
             dados = livro
         ))
    return make_response(jsonify(
        mesagem = f"Livro id: {id} não encontrado"
    ),404
    )

#PATCH - Atualizar parcialmente um livro
@app.route('/livros/<int:id>', methods=['PATCH'])
def atualizar_parcial_livro(id):
    for livro in livros:
        if livro.get('id') == id:   
            dados = request.get_json()
            livro.update(dados)
            return make_response(jsonify(
                mesagem = f"Livro id: {id} atualizado com sucesso",
                dados = livro
            ))
    return make_response(jsonify(
        mesagem = f"Livro id: {id} não encontrado"
    ),404
    )

# DELETE - Deletar um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for livro in livros:
        if livro.get('id') == id:   
            livros.remove(livro)
            return make_response(jsonify(
                mesagem = f"Livro id: {id} deletado com sucesso",
                dados = livro
            ))
    return make_response(jsonify(
        mesagem = f"Livro id: {id} não encontrado"
    ),404
    )

if __name__ == '__main__':
    app.run(debug=True)