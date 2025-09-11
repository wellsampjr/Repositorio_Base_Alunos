# Dicionário para armazenar os produtos e suas quantidades
# A chave será o nome do produto, e o valor será a quantidade disponível
estoque = {}

# Função para cadastrar um novo produto ou atualizar a quantidade de um existente
def cadastrar_produto():
    nome = input("Digite o nome do produto: ").strip().title()  # Lê o nome e padroniza
    if nome in estoque:
        print(f"Produto '{nome}' já cadastrado. Atualizando quantidade.")
    quantidade = int(input("Digite a quantidade: "))  # Lê a quantidade a ser adicionada
    estoque[nome] = estoque.get(nome, 0) + quantidade  # Soma à quantidade atual (se existir)
    print(f"Produto '{nome}' cadastrado/atualizado com sucesso.\n")

# Função para exibir todos os produtos cadastrados e suas quantidades
def listar_produtos():
    if not estoque:  # Verifica se o dicionário está vazio
        print("Estoque vazio.\n")
        return
    print("\n📦 Produtos no estoque:")
    for nome, quantidade in estoque.items():  # Percorre cada item do dicionário
        print(f"- {nome}: {quantidade}")  # Exibe nome e quantidade
    print()  # Linha em branco para espaçamento

# Função para vender um produto, ou seja, diminuir sua quantidade
def vender_produto():
    nome = input("Digite o nome do produto a vender: ").strip().title()
    
    if nome not in estoque:
        print(f"Produto '{nome}' não encontrado no estoque.\n")  # Caso o produto não exista
        return
    
    if estoque[nome] <= 0:
        print(f"Produto '{nome}' está sem estoque.\n")  # Caso esteja zerado
        return
    
    quantidade = int(input("Digite a quantidade a vender: "))
    
    if quantidade > estoque[nome]:
        # Verifica se há estoque suficiente para a venda
        print(f"Quantidade insuficiente. Temos apenas {estoque[nome]} unidades.\n")
    else:
        # Subtrai a quantidade vendida do estoque
        estoque[nome] -= quantidade
        print(f"Venda realizada: {quantidade} unidade(s) de '{nome}' vendida(s).\n")

# Função que mostra o menu principal ao usuário
def exibir_menu():
    print("=== Menu Estoque ===")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Vender Produto")
    print("4. Sair")  # Opção para encerrar o programa

# Loop principal do sistema, que roda até o usuário escolher "Sair"
while True:
    exibir_menu()  # Mostra as opções
    opcao = input("Escolha uma opção (1-4): ")

    # Estrutura condicional para tratar a escolha do usuário
    if opcao == '1':
        cadastrar_produto()  # Chama função de cadastro
    elif opcao == '2':
        listar_produtos()  # Chama função de listagem
    elif opcao == '3':
        vender_produto()  # Chama função de venda
    elif opcao == '4':
        print("Encerrando o programa. Até logo!")  # Mensagem de saída
        break  # Encerra o laço while e finaliza o programa
    else:
        # Caso a opção digitada não seja válida
        print("Opção inválida. Tente novamente.\n")

