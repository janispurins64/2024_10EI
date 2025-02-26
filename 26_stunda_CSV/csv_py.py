import csv
import os

aa = []
with open(os.getcwd()+'\\26_stunda_CSV\\dati_100.csv',newline='') as csv10ei:
    visidati = csv.reader(csv10ei,delimiter=',',quotechar='"')
    for row in visidati:
      aa.append(row)
   # 1. uzd
print(len(aa[0]))
    # 2. uzd
skaits = len(aa)-1
print(f"Ierakstu skaits: {skaits}")
# 3.uzd
# Saraksts ar vārdiem
vardi = []
with open(os.getcwd()+'\\26_stunda_CSV\\vardi.txt',mode="wt",encoding="utf8") as f1:
    for i in range(1,skaits):
        vardi.append(aa[i][2])
        f1.writelines(aa[i][2]+"\n")
# 4.uzd
vardnica_vardi = {}
for i in vardi:
    if i in vardnica_vardi.keys():
       vardnica_vardi[i] = vardnica_vardi[i] + 1
    else:
       vardnica_vardi[i] = 1 

print(vardnica_vardi)
# 5.uzd
for i in aa:
   if i[2][0] == i[3][0]:
        print(f"Pilsēta: {i[5]}")
        print(f"        Vārds: {i[2]}")
        print(f"        Uzvārds: {i[3]}")

# 6.uzd
vardu_skaits = skaits
simbolu_skaits = 0
for i in vardi:
   simbolu_skaits = simbolu_skaits + len(i)
print(f"Vārda vidējais garums: {simbolu_skaits/vardu_skaits}")
