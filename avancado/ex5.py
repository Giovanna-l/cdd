nomes = [""]*2
senhas = [0.0]*2
tam = len(nomes)
for i in range(tam):
    nomes[i] = input("digite seu nome: ")
    senhas[i] = int(input("digite sua senha: "))
for x in range(tam):
  print(f"seu nome é {nomes[x]}, sua senha é {senhas[x]}, sua posição é {x}")
