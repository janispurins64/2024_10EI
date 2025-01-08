import math
class Trissturis:
    skaits = 0
    def __init__(self,a,b,c,krasa):
        self.a = a
        self.b = b
        self.c = c
        self.krasa = krasa
        #Darbs ar klases īpašībām
        Trissturis.skaits = Trissturis.skaits + 1
    def objekts(self):
        print(f"Trīsstūra malas:  {self.a} {self.b} {self.c}")
    def perimetrs(self):
        return self.a+self.b+self.c
    def laukums(self):
        pp = (self.a+self.b+self.c)/2.
        return math.sqrt(pp*(pp-self.a)*(pp-self.b)*(pp-self.c))
#-----------------------------------

tr1 = Trissturis(5,7,8,"zila")
tr2 = Trissturis(3,4,5,"zaļa")
tr3 = Trissturis(5,7,8,"zila")
tr4 = Trissturis(3,4,5,"zaļa")
tr5 = Trissturis(5,7,8,"sarkana")
tr6 = Trissturis(3,4,5,"zaļa")
tr7 = Trissturis(5,7,8,"sarkana")
tr8 = Trissturis(3,4,5,"zaļa")
trs =[tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8]
skaits = trs.count()
for i in range(skaits):
    if