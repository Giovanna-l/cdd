nome = [""]*5
tam= len(nome)
for x in range(tam):
    nome[x]= input("digite seu nome: ")
print(nome)
"""for a in range(tam-1,-1,-1):
    print(nome[a], end=" ")"""
nome.reverse()
print(nome)