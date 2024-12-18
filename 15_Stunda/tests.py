fails = open("15_Stunda/Teksts.txt", "rt", encoding="utf-8")
dati2 = fails.read()
rindas2 = dati2.split()
vardi = len(rindas2)
fails.close()
with open("Rezultats.txt", "w", encoding="utf-8") as izvads:
  izvads.write(f"Teksta failā ir {vardi} vārdi")
