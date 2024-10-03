num = [0.0]*4
maior = -10000
menor = 10000
for x in range(4):
    num[x] = int(input("Digite um numero: "))
for i in range(4):
    if num[i]%2 == 0:
        print(num[i], end=" ")
        print()
for a in range(4):
    if num[a] > maior:
        maior = num[a]
for b in range(4):
    if num[b] < menor:
        menor = num[b]

print(f"============={maior} ")
print(f"============={menor} ")

