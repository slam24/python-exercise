class Person(object):
    def __init__(self, id=None, gender=None, age=None, height=None, weight=None, prox=None):
        self.id = id
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.prox   = prox

    def __str__(self):
        return "Usuario Nº "+str(self.id)+" -> [ Edad: "+str(self.age)+" Sexo: "+str(self.gender)+ " Peso: "+str(self.weight)+" Altura: "+str(self.height)+" ]"

    def index_mass(self):
        return float(float(self.weight)/(float(self.height)** 2))
