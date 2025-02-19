import math
class Trissturis:
    skaits = 0
    def __init__(self,a,b,c,krasa):
        self.a = a
        self.b = b
        self.c = c
        self.krasa = krasa
        self.tips = self.irtrs()
        #Darbs ar klases īpašībām
        Trissturis.skaits = Trissturis.skaits + 1
    def irtrs(self):
        if (self.a+self.b)>self.c and (self.a+self.c)>self.b and (self.b+self.c)>self.a:
            return True
        else:
            return False
    def objekts(self):
        if self.tips:
            print(f"Trīsstūra malas:  {self.a} {self.b} {self.c}")
        else:
            print(f"Trīsstūri nevar izveidot")
    def perimetrs(self):
        if self.tips:
            return self.a+self.b+self.c
        else:
            return None
    def laukums(self):
        if self.tips:
            pp = (self.a+self.b+self.c)/2.
            return math.sqrt(pp*(pp-self.a)*(pp-self.b)*(pp-self.c))
        else:
            return None
#************
class VmTrissturis(Trissturis):
    def __init__(self,a,krasa):
        self.a = a
        self.b = a
        self.c = a
        self.krasa = krasa
        self.tips = self.irtrs()
        #Darbs ar klases īpašībām
        #Trissturis.skaits = Trissturis.skaits + 1 
    def laukums(self):
        if self.tips:
            return self.a*self.a*math.sqrt(3)/4
        else:
            return None  
#-----------------------------------

tr1 = Trissturis(5,7,8,"zila")
tr2 = Trissturis(3,4,5,"zaļa")
tr3 = Trissturis(5,7,8,"zila")
tr4 = Trissturis(2,3,4,"zaļa")
tr5 = Trissturis(5,7,8,"sarkana")
tr6 = Trissturis(1,2,3,"zaļa")
tr7 = Trissturis(5,7,8,"sarkana")
tr8 = Trissturis(4,5,6,"zaļa")
trs =[tr1,tr2,tr3,tr4,tr5,tr6,tr7,tr8]
skaits = len(trs)
skaits = len(trs)
for i in range(skaits):
    if trs[i].krasa == "zaļa":
        print(f"i={i} a={trs[i].a} b={trs[i].b} c={trs[i].c}")
tr10 = Trissturis(20,5,6,"violets")
print(f"tips={tr10.tips}  S={tr10.laukums()} P={tr10.perimetrs()}")
print(f"tips={tr7.tips}  S={tr7.laukums():.3f} P={tr7.perimetrs()}")

tr21 = VmTrissturis(12,"sarkana")
print(f"tips={tr21.tips}  S={tr21.laukums()} P={tr21.perimetrs()}")