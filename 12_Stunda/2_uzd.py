fails = "12_Stunda/dati_2.txt"
with open(fails,"rt",encoding="utf8") as fin:
    dati = fin.readlines()
dati_2=[]
for a in dati:
    elements = a.strip("\n") # noņemam \n
    ele2 = elements.replace(",",".",-1)
    dati_2.append(float(ele2))
skaits = len(dati_2)
print(f"Failā ir {skaits} skatļi.")
summa = 0.0
summa2 = 0.0
for a in dati_2:
    summa = summa + a
    summa2 = summa2 + a*a
if skaits:
    print(f"Skaitļu vidējā vērtība ir {summa/skaits}.")
else:
    print(f"Skaits ir vienāds ar nulli, vavar noteikt vidējo vērtību.")  