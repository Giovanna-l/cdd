Time1 = input("Digite o nome do time 1: ")
Time2 = input("Digite o nome do time 2: ")
gol1 = int(input(f"Digite a quantidade de gol do {Time1}: "))
gol2 = int(input(f"Digite a quantidade de gol do {Time2}: "))
if gol1 == gol2 :
    print("Empate")
elif gol1 > gol2:
    print(f"{Time1} ganhou")
else:
    print(f"{Time2} ganhou")
