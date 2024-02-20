class Animal():
    def __init__(self):
        print("Animal criado")
    def comer(self):
        print("Comendo....")
    def correr(self):
        print("Correndo")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Sou um dog")
    def latir(self):
        print("Latindo...")
    def abanar_rabo(self):
        print("esta felizinho e esta abanando o rabo")


animal=Animal()
dog=Dog()

