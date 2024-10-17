from bibi import *
while True:
    opcao = int(input("digite sua opçao\n"
                      "1 para gravar\n"
                      "2 para ler\n"
                      "3 para pesquisar\n"
                      "4 para sair\n"
                      ""))
    match opcao:
        case 1:
            Gravar(input("Digite o texto: "))
        case 2:
            ler()
        case 3:
            pesquisar((input("Digite o texto para pesquisar: ")))
        case 4:
            print("Saiuu")
            break
        case _:
            print("Opção invalida!")



