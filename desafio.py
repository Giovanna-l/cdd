H1 = int(input("Digite a hora 1: "))
M1 = int(input("Digite minutos: "))
H2 = int(input("Digite a hora 2: "))
M2 = int(input("Digite os minutos 2: "))
if H1 > 12:
    H1 = H1 - 12
if H2 > 12:
    H2 = H2 -12
minutos = M1 + M2
horas = H1 + H2
if minutos >= 60:
    minutos= minutos - 60
    horas = horas + 1
if horas > 12:
    horas = horas - 12
print(f"{horas}:{minutos:02d}")
