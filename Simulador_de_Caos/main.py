import random

class Academia:
    def __init__(self):
        self.halteres=[i for i in range(10,36) if i%2==0]
        self.porta_halteres={}
        self.reniciar_o_dia()

    def reniciar_o_dia(self):
        self.porta_halteres={i:i for i in self.halteres }

    def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i!=0]
    
    def listar_espacos(self):
        return [i for i ,j in self.porta_halteres.items() if j==0 ]
    
    def pegar_halteres(self,peso):
        haltere_position=list(self.porta_halteres.values()).index(peso)
        key_haltere= list(self.porta_halteres.keys())[haltere_position]
        self.porta_halteres[key_haltere]=0
        return peso
    def devolver_halteres(self,position,peso):
        self.porta_halteres[position]=peso

    def calcular_caos(self):
        numero_caos=[i for i,j in self.porta_halteres.items() if i !=j]
        return len(numero_caos)/len(self.porta_halteres)



class Usuario:
    def __init__(self,tipo_usuario,academia):
        self.tipo_usuario=tipo_usuario
        self.peso=0
        self.academia=academia

    def iniciar_treino(self):
        lista_pesos=self.academia.listar_espacos()
        self.peso=random.choice(lista_pesos)
        self.academia.pegar_halteres(self.peso)
    
    def finalizar_treino(self):
        espaco=self.academia.listar_halteres()

        if self.tipo_usuario==1:
            if self.peso in espaco:
                position=random.choice(espaco)
                self.academia.devolver_halteres(position,self.peso)
        
        if self.tipo_usuario==2:
            position=random.choice(espaco)
            self.academia.devolver_halteres(position,self.peso)
        self.peso=0



academia=Academia()
usuarios=[Usuario(1,academia) for i in range(10)]
usuarios +=[Usuario(2,academia) for i in range(1)]

random.shuffle(usuarios)
for i in usuarios:
    random.shuffle(usuarios)
    for user in usuarios:
        user.iniciar_treino()
    for user in usuarios:
        user.finalizar_treino()

academia.porta_halteres 