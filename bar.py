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
        print()
        print(self.length)
        print(self.cs_area)
        print(self.E_modulus)
        print(self.angle)
        print(self.strain)
        print(self.stress)