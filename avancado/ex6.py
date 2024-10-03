cont=0
num = [0.0]*10
tam = len(num)
for x in range(tam):
    num[x] = int(input("Digite um numero: "))
a = int(input("digite um numero para saber quantos dele tem: "))
"""for i in range(tam):
    if num[i] == a:
        cont +=1
        print(cont)"""
print(num.count(a))
