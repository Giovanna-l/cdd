x = [0.0]*5
tam = len(x)
for i in range(tam):
   x[i] = int(input("Digite o numero: "))
for a in range(tam-1,-1,-1):
    print(x[a], end=" ")
