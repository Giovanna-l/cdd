notaalunos = 0
numAluno = int(input("Digite quantos alunos existe: "))
for x in range(1, numAluno+1):
    nota = int(input("digite a nota do aluno: "))
    notaalunos = notaalunos + nota
media = notaalunos / numAluno
print(f"a media da turma e {media:.2f}")
