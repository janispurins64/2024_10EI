import csv
import os
print("---------------------")
print(os.get_exec_path())
print("---------------------")
print(os.getcwdb())
print("---------------------")
print(os.getcwd())
print("---------------------")

with open(os.getcwd()+'\\26_stunda_CSV\\dati_100.csv',newline='') as csv10ei:
    visidati = csv.reader(csv10ei,delimiter=',',quotechar='"')
    #for row in visidati:
     #   print(row)