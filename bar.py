import utils
class Barra():

    def __init__(self, name, p1, p2, E_modulus, strain_max, stress_max, cs_area):
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.length = utils.barLength(p1,p2)
        self.cs_area = cs_area
        self.E_modulus = E_modulus
        self.angle = utils.angle(p1,p2)
        self.strain_max = strain_max
        self.stress_max = stress_max
        self.strain = None
        self.stress  = None
        self.matrix_ke = utils.matrixKe(E_modulus,cs_area,self.length,p1,p2)

    def print_properties(self):
        print("name:     ",self.name)
        print("length:   ",self.length)
        print("cs_area:  ",self.cs_area)
        print("e_modulus:",self.E_modulus)
        print("angulo:   ",self.angle)
        print("strain:   ",self.strain)
        print("stress:   ",self.stress)
    
    def get_strain_stress_string(self):
        if(self.stress > 0):
            return "TENSION"
        elif(self.stress < 0):
            return "COMPRESSION"
        else:
            return " "
    
    def String_calcIdealDimension(self):
        if(abs(self.stress) > self.stress_max):
            new_A = abs(self.cs_area*self.stress)/self.stress_max
            self.cs_area = new_A
            return ("Danger! Minimum area needed for safety factor:" +  str(new_A),1)
        return (" ",0)