import math
#Zemes nodokļa aprēķins
'''
    Vairākrindu komentārs
    Funkcija malas garuma aprēķinam
'''
def malas_garums(ax, ay, bx, by):
    return math.sqrt((ax-bx)*(ax-bx)+(ay-by)*(ay-by))

# A, B, O koordinātas
a_x = 0.0
a_y = 0.0
b_x = 1.0
b_y = 4.0
o_x = 4.0
o_y = 1.0

mala_a = malas_garums(o_x, o_y, b_x, b_y)
mala_b = malas_garums(o_x, o_y, a_x, a_y)
mala_o = malas_garums(a_x, a_y, b_x, b_y)


print(f"Mala a={mala_a}")
print(f"Mala b={mala_b}")
print(f"Mala o={mala_o}")