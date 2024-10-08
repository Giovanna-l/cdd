N = []
S = []
op = 0
while op != 3:
    print("\nSistema de Login:")
    print("1. Cadastrar")
    print("2. Login")
    print("3. Sair")
    op = int(input("Escolha uma opção (1, 2 ou 3): "))
    if op == 1:
        nome = input("Digite o nome do usuário: ")
        senha = int(input(f"Digite a senha para o usuário {nome}: "))
        N.append(nome)
        S.append(senha)
        print(f"Usuário {nome} cadastrado com sucesso!")
    elif op == 2:
        nome = input("Digite o nome de usuário: ")
        senha = int(input("Digite a sua senha: "))
        if nome in N:
            indice = N.index(nome)
            if S[indice] == senha:
                print(f"Login concluido com sucesso! Bem-vindo(a), {nome}.")
            else:
                print("Senha incorreta!")
        else:
            print("Usuário não encontrado!")
    elif op == 3:
        print("Saindo...")

    else:
        print("Opção inválida, tente novamente.")