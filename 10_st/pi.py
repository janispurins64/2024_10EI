fails = "C:/Users/jpurins/Desktop/2024_10EI/10_st/teksts.txt"
with open(fails,"rt",encoding="utf8") as dd:
    dati = dd.readlines()
    print(f"--- {dati}")
