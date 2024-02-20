

class Cirle:
    def __init__(self,raio=1):
        self.raio=raio
    def calcular_area(self):
        resul=self.raio*self.raio*3.14
        return  resul

    def retornar_raio(self):
        return self.raio


c1=Cirle(2)
c2=Cirle(10)
print(c1.retornar_raio())
print(c2.calcular_area())

