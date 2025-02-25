import csv
import os

with open(os.getcwd()+'\\26_stunda_CSV\\dati_100.csv',newline='') as csv10ei:
    visidati = csv.reader(csv10ei,delimiter=',',quotechar='"')
    for row in visidati:
       print(row)