class kubs:
    #2.2. uzd
    def __init__(self, mala: int, krasa: str):
        #kontrole
        #if mala
        self.malas_garums = mala
        
        self.krasas_nosaukums = krasa   
    #--------------------------------    
    def aprekinat_tilpumu(self):
        return self.malas_garums**3
    def __del__(self):
        print(f"Likvidēts kubs, kura krāsa ir {self.krasas_nosaukums}")

#2.3 uzd
kubg = kubs()
kubg.izveidot(10,"zaļa")
#2.3a uzd
kubg1 = kubs(12.3,"zila")


#xx uzd
del kubg


