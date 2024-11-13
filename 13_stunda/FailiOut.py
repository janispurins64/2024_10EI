print("Teksta faili: datu izvads")
import math

def laukums(a=0.0, b=1.0, n=1):
    if n==0: return 0

    d = (b-a)/n
    laukums = 0.0
    x = a
    for i in range(n):
        laukums = laukums + math.sqrt(b*b-x*x)
        x = x + d
    laukums = laukums * d
    return laukums
s = laukums(0.0, 1.0,1000)*4.0
print(f"Laukums={s}")
print(f"Relatīvā kļūda: {(s/math.pi-1)*100}%")


    