""" Nome: Matheus Bezerra Domingos
    Data: 20/11/2024
    Objetivo: "Fazer um programa que solicite o nome e 3 notas para calcular a media e mostrar se foi aprovado ou não"
"""

# vou precisar da qunatidades de alunos para o for
# informações soobre eles: nome, media das 3 notas


# Solicita ao usuario a quantidades de alunos para ser analisado
qnts_alunos = int(input("Digite a quantidades de alunos: "))


#armazena os nomes, notas, medias e o status
nomes = []
notas1 = []
notas2 = []
notas3 = []
medias = []
status = []


print("\n")

#Usando o for para escrever os nomes e as notas dos alunos
for i in range(qnts_alunos):
    
    #nome do aluno
    nome = input(f"Digite o nome do {i+1} aluno..: ")
    nomes.append(nome)
    
    #Primeira nota do aluno
    nota1 = float(input(f"Digite a primeira nota do {i+1} aluno..: "))
    notas1.append(nota1)  #adiciona a nota1 dentro da lista de notas1

    #Segunda nota do aluno
    nota2 = float(input(f"Digite a segunda nota do {i+1} aluno..: "))
    notas2.append(nota2)  #adiciona a nota2 dentro da lista de notas2
    
    #Terceira nota do aluno
    nota3 = float(input(f"Digite a terceira nota do {i+1} aluno..: "))
    notas3.append(nota3)  #adiciona a nota3 dentro da lista de notas3

    #Pega todas as notas e divide por 3
    media = (nota1 + nota2 + nota3) / 3
    medias.append(media) #adiciona a media dentro da lista de medias

    if media >= 6: #verifica se o aluno foi aprovado ou não
        status.append("Aprovado") #se sim, atualiza o status da lista 
    else:
        status.append("rerovado")
    
    print("\n") #pula uma linha

for i in range(qnts_alunos): #onde esta relacionado a quantidades de alunos e as notas tbm, precisa do "i"
    print(f"O/A aluno/a {nomes[i]} ficou com a média {medias[i]:.1f} e foi {status[i]}")

