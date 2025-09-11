#Criamos uma lista com as infoemações dos alunos    

alunos = [
    {"nome": "João", "idade":20, "nota":7.5},
    {"nome": "Maria", "idade":18, "nota":9.5},
    {"nome": "Pedro", "idade":22, "nota":8.2},
    {"nome": "Ana", "idade":21, "nota":7.9}
   
]

totalNotas = 0 # essa variavel será nosso contador para somar as notas dos alunos 
quantidadeAlunos = len(alunos) #essa vai informar a quantidade de alunos atraves do len 

for aluno in alunos:
    totalNotas += aluno["nota"]
mediaNotas = totalNotas / quantidadeAlunos
print(f"A media das notas dos alunos é {mediaNotas:.2f}")