# Crie um sistema de login simples em Python, onde o usúario precisará
# inserir um nome de usúario e senha para acessar o sistema.

# Dados de login
usuario_cadastrado = "usuario123"
senha_cadastrada = "senha123"

# Solicitar nome de usúario e senha
nome_usuario = input("Digite seu nome de usúario: ").strip().lower()
senha = input("Digite sua senha: ").strip().lower()

# Verificação do login
if nome_usuario == usuario_cadastrado and senha == senha_cadastrada:
   print("Login bem sucedido! Bem-vinda(a)", nome_usuario)
else:
   print("Nome de usúario ou senha incorreto. Tente Novamente.")