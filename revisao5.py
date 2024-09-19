peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))
imc = peso / (alt)**2
if imc < 18.6:
    print("Abaixo do peso")
elif imc == 18.6 or imc < 25:
    print("Peso ideal(parabens)")
elif imc == 25 or imc < 30:
    print("Levemente acima do peso")
elif imc == 30 or imc < 35:
    print("Obesidade grau I")
elif imc == 35 or imc < 40:
    print("Obesidade grau II(severa)")
else:
    print("Obesidade grau III(morbida)")

