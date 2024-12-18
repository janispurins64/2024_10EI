alfabets = ['A','Ā','B','C','Č','D','E','Ē','F','G','Ģ','H','I','Ī','J','K','Ķ','L','Ļ',
    'M','N','Ņ','O','P','R','S','Š','T','U','Ū','V','Z','Ž']

def varda_ievads():
    # 2.1 Vārda ievads
    while 1:
        vards = input("Ievadiet vārdu:")

        #2.2 Ir tikai atļautās vērtības
        #2.3 Vai ir tikai viens vārds
        for i in vards:
            if i.upper()  in alfabets:
                if i[0] in alfabets:
                   #2.4 Vai pirmais burts ir lielais
                   return vards
                else:
                    print("Vārdam pirmais birts nav lielais")
                    print("Atkārtojiet datu ievadu")
            else:
                print("Ievadītais teksts satur vairāk par vienu vārdu vai neatļautus simbolus")
                print("Atkārtojiet datu ievadu")
#2.6 Alfabēts
analfabets = {'A': 1, 'Ā': 2, 'B': 3, 'C': 4, 'Č': 5, 'D': 6, 'E': 7, 'Ē': 8, 'F': 9, 'G': 10,
    'Ģ': 11, 'H': 12, 'I': 13, 'Ī': 14, 'J': 15, 'K': 16, 'Ķ': 17, 'L': 18, 'Ļ': 19,
    'M': 20, 'N': 21, 'Ņ': 22, 'O': 23, 'P': 24, 'R': 25, 'S': 26, 'Š': 27, 'T': 28,
    'U': 29, 'Ū': 30, 'V': 31, 'Z': 32, 'Ž': 33}
print("Alfabēts ar kārtas nunuriem izveidots") #2.12
#2.7 Izveidojam jaunu sarakstu
saraksts = []
for i in range(34):
    saraksts.append(None)
print("Jauns tukšs saraksts izveidots")
while 1:
    #Ievadam un pārbaudam vārdu
    cc = varda_ievads()
    #2.8, 
    indekss = analfabets[cc[0]]  #Atrodam indeksu alfabētā
    #2.9
    print(f"Indekss: {indekss}")
    if saraksts[indekss] == None:
        print(f"Sarakta elementā ar indeksu {indekss} ievietojam jaunu vērtību")
    else:
        print(f"Sarakta elementā ar indeksu {indekss} aizvietojam ar jaunu vērtību")
    saraksts[indekss] = cc 
    if saraksts.count(None) == 1:
        print(f"Saraksts ir aizpildīts: {saraksts}")      