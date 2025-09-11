# Criar um jogo da forca onde o usuáro tenta adivinhar uma palavra secreta,
#  letra por letra, com até 6 erros permitidos

import random

def jogar ():  #função principal

    imprimir_mensagem_abertura() #funcao para mensagem de abertura

    palavra_secreta = carregar_palavra_secreta() #escolhe uma palavra aleatória de um arquivo.txt
    letras_acertadas = inicializa_letras_acertadas((palavra_secreta)) #transforma a palavras em  uma
    #lista de "_", para cada letra (ocultando a palavra)

    print(letras_acertadas) # Mostra ao jogador os espaços da palavra, representados po underline (_ _ _)

# Variaveis de controle

    enforcou = False #torna-se verdadeiro ao jogador errar 6 vezes
    acertou = False # verdadeiro se o jogador acertar todas as letras 
    erros  = 0 # conta o umero de tentativas erradas

    while (not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra ):
                    letras_acertadas[index] = letra
                index += 1 
        
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("VOCÊ GANHOU !!")
    
    else:
        print("VOCÊ PERDEU!!")
    
    print("Fim de jogo")

def pede_chute():
    chute = input("Qual a letra ?: ")
    chute = chute.strip().upper()
    return chute

def imprimir_mensagem_abertura ():
    print("**********************************")
    print("*** Bem vindo ao jogo da Forca ***")
    print("**********************************")

def carregar_palavra_secreta(nome_do_arquivo = "C:/Users/Aluno_Programador/Documents/Wellington Sampaio/jogo/Atividade 29 - palavras_forca.txt"):
    arquivo = open(nome_do_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return["_" for letra in palavra]

# Contextualizar o método "if (__name == "__main__"):"significa que o arquivo 

if (__name__ == "__main__"):
    jogar()


    