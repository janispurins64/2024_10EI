#Sakņu precizēšana ar intervāla dalīšanu uz pusēm
# -4,-1
import math

def y(x):
    return x*x*x+3*x*x-1
a = -4
b = -1
delta = 0.001
while 1:

    c = (a+b)/2
    ya = y(a)
    yb = y(b)
    yc = y(c)
    if ya == 0:
        sakne = a
        break
    if yb == 0:
        sakne = b
        break 
    if yc == 0:
        sakne = c
        break
    if abs(ya-yb)<delta:
        sakne = c
        break
                    
    if ya*yc > 0:
        a = c
    else:
        b = c
print(f"Sakne ir {sakne:.5f}")