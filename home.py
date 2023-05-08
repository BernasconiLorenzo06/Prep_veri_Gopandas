
from flask import Flask, render_template, request
app = Flask(__name__)

import os

@app.route('/')
def home():
    import pandas as pd
    df = pd.read_excel('https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true')
    return render_template('home.html')



@app.route('/esercizio1',methods = ["GET"])
def esercizio1():
   import pandas as pd
   df = pd.read_excel('https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true')
   quartiere = request.args.get('quartiere')
   table = df[df["neighborhood"] == quartiere]
   tabella = table.to_html()
   return render_template('esercizio1.html', tabella = tabella)

@app.route('/esercizio2',methods = ["GET"])
def esercizio2():
   import pandas as pd
   df = pd.read_excel('https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true')
   dfquartieri = df[["neighborhood"]].sort_values(by="neighborhood")
   a = set(df['neighborhood'])
   table = list(a)
   return render_template('esercizio2.html', tabella = table)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)