combustivel= input("Digite qual combustivel voce escolheu E para etanol e G para gasolina? ")
litros = float(input("Digite quantos litros voce colocou? "))

if combustivel == "G" or combustivel== "g":
    valor = litros * 5.8
elif combustivel== "E" or combustivel== "e":
    valor = litros * 4.9
else:
    print("combustivel invalido")
print(f"voce gastou {valor} reais")