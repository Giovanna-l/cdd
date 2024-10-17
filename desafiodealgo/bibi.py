"""with open("NomesTurmaC.txt", "a") as arquivo:
    nome = input("Digite um nome: ")
    arquivo.write(f"{nome}\n")


with open("NomesTurmaC.txt", "r") as arquivos2:
    print(arquivos2.read())"""
def Gravar(t):
    with open("NomesTurmaC.txt", "a") as arquivo:
        arquivo.write(f"{t}\n")
def ler():
    with open("NomesTurmaC.txt", "r") as arquivos2:
        print(arquivos2.read())

def pesquisar(texto):
    cont=0
    with open("NomesTurmaC.txt", "r") as pes:
        for x in pes:
            if texto in x:
                cont += 1

        print(f"Achei {cont} ocorrencia {texto} no arquivo")