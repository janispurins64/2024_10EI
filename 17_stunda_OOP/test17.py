class Pirma:
    def __init__(self, vecums, masa):
        self._vecums = vecums
        self.__masa = masa
    
    def get_masa(self):
        return self.__masa
    def set_masa(self,masa):
        self.__masa = masa   

mu = Pirma(13,12)
print(f"Atribūts vecums {mu._vecums}")
print(f"Atribūts masa {mu.get_masa()}")
mu.set_masa(46)
print(f"Atribūts masa {mu.get_masa()}")