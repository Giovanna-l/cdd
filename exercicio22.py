x= 1
while x == 1:
    n1 = float(input("Digite a nota 1: "))
    while n1 < 0 or n1 > 10:
        n1 = float(input("Digite a nota 1: "))

    n2 = float(input("digite a nota 2: "))
    while n2 < 0 or n2 > 10:
        n2 = float(input("Digite a nota 2: "))

    media = (n1 + n2)/ 2
    print(media)
    x = int(input("Deseja realizar novo calculo?\n"
                  "digite 1 para sim e 2 para nao: "))
print("finalizado")



