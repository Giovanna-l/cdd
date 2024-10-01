A = [0.0]*10
M = [0.0]*10
tam = len(A)
for i in range(tam):
    A[i] = int(input("Digite o numero: "))
x = float(input("Digite um numero para ser o multiplicador: "))
for a in range(tam):
    M[a] = x * A[a]
print(A)
print(x)
print(M)


