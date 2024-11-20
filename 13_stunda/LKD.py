#Programma nosaka divu skaitļu lielāko kopīgo dalītāju
a = int(input("Ievadi pirmo skaitli:"))
b = int(input("Ievadi otru skaitli:"))

#Eiklīda algoritms
while 1:
    atl = a % b  #Atlikums
    if not atl:
        break
    a = b
    b = atl
print(f"LKD: {b}")