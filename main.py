import utils


class Barra():

    def __init__(self, p1, p2, E_modulus, cs_area):
        self.p1 = p1
        self.p2 = p2
        self.length = utils.barLength(p1,p2)
        self.cs_area = cs_area
        self.E_modulus = E_modulus
        self.angle = utils.angle(p1,p2)
        self.strain = None
        self.stress = None 


