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
with open("Rezultats.txt","wt",encoding="utf8") as f1:
    f1.write("Riņķa laukums, atkarībā no intervālu skaita:\n")
    f1.write("  n       S    RK(%)\n")
    for i in range(2,301,20):
        s = laukums(0.0, 1.0,i)*4.0
        rk = (s/math.pi-1)*100
        f1.write(f"{i:3d}{s:8.2f}{rk:6.0f}\n")


    