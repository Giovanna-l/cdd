import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turma_c"
)
meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()
for x in resultado:
    print(x)
nome1= input("digite nome: ")
telefone1= int(input("digite o numero: "))
sql = "insert into alunos (nome, telefone) values (%s,%s)"
data = (nome1, telefone1)
meucursor.execute(sql,data)
banco.commit()
meucursor.close()
banco.close()