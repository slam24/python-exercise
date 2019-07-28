class Person(object):
    def __init__(self, id=None, gender=None, old=None, height=None, weight=None, prox=None):
        self.id = id
        self.gender = gender
        self.old = old
        self.height = height
        self.weight = weight
        self.prox   = prox

    def __str__(self):
        return "Usuario Nº "+str(self.id)+" -> [ Edad: "+self.old+" Sexo: "+self.gender+ " Peso: "+self.weight+" Altura: "+self.height+" ]"

    def index_mass(self):
        return float(float(self.weight)/(float(self.height)** 2))
