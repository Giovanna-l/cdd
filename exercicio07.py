n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
media =  (n1+n2+n3)/3
if media>=7 :
    print(f"Aprovado com a media {media}")

else:
    if media >=4:
        print(f"Recuperaçao com a media {media} ")

    else:
        print(f"Reprovado com a media {media}")


