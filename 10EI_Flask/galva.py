from flask import Flask,g
from flask import request
from flask import render_template
import random
import datetime
import csv
import os

app = Flask(__name__)

@app.route('/tests')
def health():
    return 'Serveris ir startēts'

@app.route('/sveiciens')
def sveicu():
    return render_template('sveiciens.html')

@app.route('/suminajums') #Pirmais variants
def suminajums():
    vardi =['Juris','Vilis','Agris','Kristaps','Alberts','Pēteris','Alnis','Vilnis','Kārlis','Māris'] 
    i = random.randint(0,9)
    return render_template('uzruna.html',vards=vardi[i])

@app.route('/suminajums2') #Variants ar vārdnīcu
def suminajums2():
    vardi2 =[{'vards':'Juris','dz':'v'},{'vards':'Vilis','dz':'v'},{'vards':'Ieva','dz':'s'},
             {'vards':'Agris','dz':'v'},{'vards':'Ilze','dz':'s'}] 
    i = random.randint(0,4)
    if vardi2[i]['dz'] == 'v':
        te = 'Sumināts'
    else:
        te = 'Sumināta'
    laiks = datetime.datetime.now() # Nolasām sistēmas laiku
    laiks2 = laiks.strftime("%H:%M:%S") # Izvadām tikai stundas, minūtes un sekundes
    return render_template('uzruna2.html',vards=vardi2[i]['vards'],teksts=te, t=laiks2)

@app.route('/dati') #Trīsstūra malas
def dati():
   return render_template("dati.html") 

@app.route('/dati2',methods=['GET','POST']) #Trīsstūra malas
def dati2():
   a = request.args.get('mala_a') # Tiek izmantots input atribūts name
   b = request.args.get('mala_b') # Tiek izmantots input atribūts name   
   c = request.args.get('mala_c') # Tiek izmantots input atribūts name
   print(f"Mala a= {a}")
   print(f"Mala b= {b}") 
   print(f"Mala c= {c}")
 
   a1,b1,c1 = malas_2(a,b,c)
   print(trisTips(a1, b1, c1))
   dati_w_csv(a1,b1,c1)
   return render_template("dati.html") 

#----------------------------- Funkcijas
def dati_w_csv(a,b,c):
    if irTrissturis(a, b, c):
        dati = [a,b,c,'1',trisTips(a, b, c),trisATips(a, b, c)]
    else:
        dati = [a,b,c,'0','','']
    with open(os.getcwd()+'\\10EI_Flask\\static\\dati.csv','+a',encoding="UTF8",newline='') as file1:
        write = csv.writer(file1)     
        write.writerow(dati)

    return

def dati_r_csv(dati):
    return
def malas_2(a,b,c):
    if isinstance(a, (int, float, str)):
        aa = float(a)
    else:
        aa = 0.
    if isinstance(b, (int, float, str)):
        bb = float(b)
    else:
        bb = 0.
    if isinstance(c, (int, float, str)):
        cc = float(c)
    else:
        cc = 0.
    return aa,bb,cc


def irTrissturis(a, b, c):
    if a<(b+c) and b<(c+a) and c<(a+b):
        return True
    else:
        return False

def trisTips(a, b, c):
    malas = [a, b, c]
    malas.sort()
    if c*c>(a*a+b*b):
        return "Platleņķa"
    elif c*c<(a*a+b*b):
        return "Šaurleņķa"
    else:
        return "Taisnleņķa"        
def trisATips(a, b, c):
    malas = [a, b, c]
    malas.sort()
    if a==c:
        return "Vienādmalu"
    elif a==b or b==c:
        return "Vienādsānu"
    else:
        return "Dažādmalu"     

if __name__ == '__main__':
    app.run(debug=True, port=5000)