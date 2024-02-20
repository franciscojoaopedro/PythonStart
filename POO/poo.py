


class Dog():
    def __init__(self,raca):
        self.raca:str=raca
        self.cor:str="Castanho"
        self.idade=10
        print("O dog e {}".format(raca))

    def envelhecer(self):
        print("Envelhecer")


dog=Dog("Lab")
dog.envelhecer()