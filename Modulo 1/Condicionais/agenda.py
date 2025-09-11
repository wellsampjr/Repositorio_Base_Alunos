# Programa Cadastro 

# Lista onde os contatos serão armazenados
agenda = []

# Função para exibir o menu
def mostrar_menu():
    print("\n--- MENU ---")
    print("[1] Cadastrar pessoa")
    print("[2] Listar pessoas")
    print("[3] Excluir pessoa")
    print("[0] Sair")

# Função para verificar se o nome já existe na agenda
def nome_existe(nome):
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            return True
    return False

# Função para cadastrar uma nova pessoa
def cadastrar_pessoa():
    nome = input("Digite o nome: ").strip()

    if nome_existe(nome):
        print(f"{nome} já está cadastrado na agenda.")
    else:
        telefone = input("Digite o telefone: ").strip()
        email = input("Digite o e-mail: ").strip()

        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }

        agenda.append(contato)
        print(f"{nome} foi cadastrado com sucesso.")

# Função para listar todos os contatos
def listar_pessoas():
    if agenda:
        print("\n--- Lista de Contatos ---")
        for i, contato in enumerate(agenda, start=1):
            print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
    else:
        print("A agenda está vazia.")

# Função para excluir uma pessoa pelo nome
def excluir_pessoa():
    nome = input("Digite o nome da pessoa a ser excluída: ").strip()
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)
            print(f"{nome} foi removido da agenda.") 
            return
    print(f"{nome} não foi encontrado na agenda.")

# Função principal que executa o menu e chama as demais
def executar_programa():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            excluir_pessoa()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do programa
executar_programa()
