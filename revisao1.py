x = 1
while x == 1:
    num = int(input("digite um valor: "))
    if num % 2 != 0:
        if num < 0:
            print(f"{num} é impar e negativo")
        else:
            print(f"{num} é impar e positivo")
    else:
        if num > 0:
            print(f"{num} par")
    x = int(input("deseja repetir\n"
                  "1 sim\n"
                  "2 nao: "))
print("finalizado")