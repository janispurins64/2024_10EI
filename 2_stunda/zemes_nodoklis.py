import math
#Zemes nodokļa aprēķins
'''
    Vairākrindu komentārs
    Funkcija malas garuma aprēķinam
'''
def malas_garums(a: list, b: list):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))

# Funkcija laukuma aprēķinam
def laukums(a: float, b: float, c: float):
    p = (a+b+c)/2.0
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

lauks = [[5.0, 0.0],[4.98, 0.26],[4.92, 0.52],[4.83, 0.78],[4.7, 1.03],[4.53, 1.27],[4.33, 1.5],[4.1, 1.72],[3.83, 1.93],[3.54, 2.12],[3.21, 2.3],[2.87, 2.46],[2.5, 2.6],[2.11, 2.72],[1.71, 2.82],[1.29, 2.9],[0.87, 2.95],[0.44, 2.99],[0.0, 3.0],[-0.44, 2.99],[-0.87, 2.95],[-1.29, 2.9],[-1.71, 2.82],[-2.11, 2.72],[-2.5, 2.6],[-2.87, 2.46],[-3.21, 2.3],[-3.54, 2.12],[-3.83, 1.93],[-4.1, 1.72],[-4.33, 1.5],[-4.53, 1.27],[-4.7, 1.03],[-4.83, 0.78],[-4.92, 0.52],[-4.98, 0.26],[-5.0, 0.0],[-4.98, -0.26],[-4.92, -0.52],[-4.83, -0.78],[-4.7, -1.03],[-4.53, -1.27],[-4.33, -1.5],[-4.1, -1.72],[-3.83, -1.93],[-3.54, -2.12],[-3.21, -2.3],[-2.87, -2.46],[-2.5, -2.6],[-2.11, -2.72],[-1.71, -2.82],[-1.29, -2.9],[-0.87, -2.95],[-0.44, -2.99],[-0.0, -3.0],[0.44, -2.99],[0.87, -2.95],[1.29, -2.9],[1.71, -2.82],[2.11, -2.72],[2.5, -2.6],[2.87, -2.46],[3.21, -2.3],[3.54, -2.12],[3.83, -1.93],[4.1, -1.72],[4.33, -1.5],[4.53, -1.27],[4.7, -1.03],[4.83, -0.78],[4.92, -0.52],[4.98, -0.26],[5.0, -0.0]]


for el in lauks:
    print(f"--->  {el}")


# A, B, O koordinātas 1.trs.
a = [0.0, 0.0]
b = [0.0, 10.0]
o = [15.0, 5.0]

mala_a = malas_garums(o, b)
mala_b = malas_garums(o, a)
mala_o = malas_garums(a, b)
laukums_1 = laukums(mala_a, mala_b, mala_o)

print(f"Trīsstūta laukums S={laukums_1}")
# A, B, O koordinātas 2.trs.
a = [0.0, 10.0]
b = [30.0, 10.0]
o = [15.0, 5.0]

mala_a = malas_garums(o, b)
mala_b = malas_garums(o, a)
mala_o = malas_garums(a, b)
laukums_2 = laukums(mala_a, mala_b, mala_o)

print(f"Trīsstūta laukums S={laukums_2}")
# A, B, O koordinātas 3.trs.
a = [30.0, 10.0]
b = [30.0, 0.0]
o = [15.0, 5.0]

mala_a = malas_garums(o, b)
mala_b = malas_garums(o, a)
mala_o = malas_garums(a, b)
laukums_3 = laukums(mala_a, mala_b, mala_o)

print(f"Trīsstūta laukums S={laukums_3}")

# A, B, O koordinātas 4.trs.
a = [30.0, 0.0]
b = [0.0, 0.0]
o = [15.0, 5.0]

mala_a = malas_garums(o, b)
mala_b = malas_garums(o, a)
mala_o = malas_garums(a, b)
laukums_4 = laukums(mala_a, mala_b, mala_o)

print(f"Trīsstūta laukums S={laukums_4}")

print(f"Lauka laukums S={laukums_1+laukums_2+laukums_3+laukums_4}")

