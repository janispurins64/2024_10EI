from flask import Flask,g
from flask import request
from flask import render_template
import random
import datetime

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
   print(f"Mala a= {a}") 
   return render_template("dati.html") 

if __name__ == '__main__':
    app.run(debug=True, port=5000)