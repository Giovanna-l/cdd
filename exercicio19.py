opcao = 1
while opcao==1:
    num1 = float(input("Digite o n1: "))
    num2 = float(input("Digite o n2: "))
    while num2 == 0:
        num2 = float(input("numero invalido, digite o n2: "))
    resultado = num1 / num2
    print(resultado)
    opcao = int(input("Deseja continuar: \n"
                      "1 para sim\n"
                      "2 para nao\n"))
print('encerrou')