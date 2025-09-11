from random import randrange
#from click import clear

def exibir_tabuleiro(tabuleiro):
    #clear()
    print("+-------"*3, "+", sep="")# Limpa a tela e imprimi a borda superior do tabuleiro 
    for linha in range(3):
        print("|       " *3,"|", sep="")
        for coluna in range(3):
            print("|    "+str(tabuleiro[linha][coluna])+"  ",end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="") 

def entrada_jogador(tabuleiro):
    valido = False 
    while not valido:
        movimento = input("Digite seu movimento: ")
        valido = len(movimento) == 1 and movimento >= "1" and movimento <= "9"
        if not valido:
            print("Movimento ruim - repita sua entrada!")
            continue
        movimento = int(movimento) -1 #converse para índice de 0 a 8
        linha = movimento // 3
        coluna = movimento % 3 
        conteudo = tabuleiro[linha][coluna] # Verifica o conteúdo do campo selecionado 
        valido = conteudo not in ["O","X"]

        if not valido:
            print("Campo já ocupado - repita sua entrada!")
            continue
        tabuleiro[linha][coluna] = "O"

def lista_campos_livers(tabuleiro):
    livres = [] # Lista inicialmente vazia 
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ["O", "X"]:
                livres.append((linha,coluna))
    return livres

def verifica_vitoria(tabuleiro, sinal):
    if sinal == "X":
        vencedor = "computador"
    elif sinal == "O":
        vencedor = "jogador"
    else:
        vencedor = None 
    diag1 = diag2 = True #variaveis para verificar as diagonais 
    for  i in range(3):
        # Verifica a linha i
        if tabuleiro[i][0] == sinal and tabuleiro[i][1] == sinal and tabuleiro [i][2] == sinal:
            return vencedor
        # Verifica a coluna i
        if tabuleiro[0][i] == sinal and tabuleiro[1][i] == sinal and tabuleiro [2][i] == sinal:
            return vencedor
        # Verifica a diagonal principal
        if tabuleiro [i][i] != sinal:
            diag1 = False
        # Verifica a diagonal inversa
        if tabuleiro [i][2 - 1] != sinal:
            diag2 = False
    
    if diag1 or diag2:  
        return vencedor
    return None

def jogada_computador(tabuleiro):
    livres = lista_campos_livers(tabuleiro) 
    quantidade = len(livres)
    if quantidade > 0 :
        escolha = randrange(quantidade)
        linha, coluna = livres[escolha]
        tabuleiro[linha][coluna]  = "X"
    
#Cria o tabuleiro inicial com números de 1 a 9 
tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tabuleiro[1][1] = "X" # define um "X" no centro 
livres  = lista_campos_livers(tabuleiro)
vez_jogador = True # Indica que é a vez do jogador
vencedor = None # Variavel para armazenar o vencedor 
    
while len(livres) and vencedor is None: # looping que verifica se há espaços vazios ninguem vence
    exibir_tabuleiro(tabuleiro)
    if vez_jogador:
        entrada_jogador(tabuleiro)
        vencedor = verifica_vitoria(tabuleiro, "O")
    else:
        jogada_computador(tabuleiro)
        vencedor = verifica_vitoria(tabuleiro, "X")
    vez_jogador = not vez_jogador # aletera os jogadores
    livres = lista_campos_livers(tabuleiro)

exibir_tabuleiro(tabuleiro) #exibicao dos resultador 
if vencedor == "jogador":
    print("Você Ganhou!")
elif vencedor == "computador":
    print("Eu Venci!")
else: 
    print("Empate!")

