class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.dormindo = False
        self.andando= False

    def comer(self):
        if self.comendo == False:
           if self.andando == False:
               if self.dormindo == False:
                   print(f"{self.nome} foi comer")
                   self.comendo = True
               else:
                   print(f"{self.nome} não foi comer pq esta dormindo")
           else:
               print(f"{self.nome} não foi comer pq esta andando")
        else:
            print(f"{self.nome} não foi comer pq ja esta comendo ")
    def andar(self):
        if self.comendo == False:
           if self.andando == False:
               if self.dormindo == False:
                   print(f"{self.nome} foi andar")
                   self.andando = True
               else:
                   print(f"{self.nome} não foi andar pq esta dormindo")
           else:
               print(f"{self.nome} não foi andar pq esta comendo")
        else:
            print(f"{self.nome} não foi andar pq ja esta andando ")
    def dormir(self):
        if self.comendo == False:
           if self.andando == False:
               if self.dormindo == False:
                   print(f"{self.nome} foi dormir")
                   self.dormindo = True
               else:
                   print(f"{self.nome} não foi dormir pq esta comendo")
           else:
               print(f"{self.nome} não foi dormir pq esta andando")
        else:
            print(f"{self.nome} não foi dormir pq ja esta dormindo ")

class Animal:
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f"O {self.nome} foi comer")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome} foi miando...")

    def comer(self):
        print(f"O gato {self.nome} foi comer")
class Cachorro(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def latir(self):
        print(f"O {self.nome} foi latindo")
    def comer(self):
        print(f" O Cachorro {self.nome} foi comer")
class Coelho(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def pula(self):
        print(f"O {self.nome} foi pulando")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def mu(self):
        print(f"A vaca {self.nome} foi mumu")