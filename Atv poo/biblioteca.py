class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.dormindo = False
        self.andando= False

    def andar(self):
        if self.comendo != False:
            print("Ele esta comendo")
        elif self.dormindo != False:
            print("Ele esta dormindo")
        elif self.andando == False:
            self.andando = True
            print("Ele esta andando")
        else:
            print(f"{self.nome} já esta andando")


    def comer(self):
        print(f"{self.nome} foi comer")

    def dormi(self):
        print(f"{self.nome}foi dormir")