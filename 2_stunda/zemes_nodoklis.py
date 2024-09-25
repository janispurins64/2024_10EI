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

