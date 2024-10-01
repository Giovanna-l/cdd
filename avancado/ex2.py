notas = [""]*5
tam = len(notas)
for x in range(tam):
    notas[x] = int(input("digite a nota: "))
soma = 0
for i in range(tam):
    soma += notas[i]
media = soma/tam
cont =0
for a in range(tam):
    if notas[a] > media:
        cont += 1
print(f"A media da turma é {media} e {cont} aulunos tiveram nota maior que a media")
