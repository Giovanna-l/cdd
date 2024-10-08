def impar (n):
    if n % 2 != 0:
        print("numero impar")
def imprimeNome(nome):
    print(f"nome: {nome}")
def piramide(num):
    for i in range(1, num + 1, ):
        for a in range(i):
            print(i, end=" ")
        print()
def piramide2(num):
    for i in range(1, num + 1, ):
        for a in range(i):
            print(a, end=" ")
        print()
def vogais(letras):
    cont=0
    t = len(letras)
    for x in range(t):
        if letras[x] in "aeiouAEIOU":
            cont +=1
    print(f"encontrei {cont} vogais ")

def soma(*numeros):
   ta = len(numeros)
   soma = 0
   for y in range(ta):
       soma += numeros[y]
   print(soma)


def text(tex):
    tam= len(tex)
    conta=tam
    for a in range(tam):
        if tex[a] == " ":
           conta -=1
    print(conta)
    for k in range(tam-1, -1,-1):
        print(tex[k], end=" ")

def listaUnica(l):
     novalista=[]
     for j in l:
         if j not in novalista:
             novalista.append(j)
     print(novalista)
def testprimo(n)
    if (n==1):
        return n, "não ´pe primo"








