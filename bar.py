import utils
class Barra():

    def __init__(self, name, p1, p2, E_modulus, strain, stress, cs_area):
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.length = utils.barLength(p1,p2)
        self.cs_area = cs_area
        self.E_modulus = E_modulus
        self.angle = utils.angle(p1,p2)
        self.strain = strain
        self.stress = stress 

    def print_properties(self):
        print("name:     ",self.name)
        print("length:   ",self.length)
        print("cs_area:  ",self.cs_area)
        print("e_modulus:",self.E_modulus)
        print("angulo:   ",self.angle)
        print("strain:   ",self.strain)
        print("stress:   ",self.stress)