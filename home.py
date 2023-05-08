
from flask import Flask, render_template, request
app = Flask(__name__)

import os
import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import contextily

provincie = geopandas.read_file("province/ProvCM01012022_g_WGS84.dbf")
provincie3857 = provincie.to_crs(epsg=3857)
comuni = geopandas.read_file("comuni/Com01012022_g_WGS84.dbf")
comuni3857 = comuni.to_crs(epsg=3857)

@app.route('/')
def home():
   return render_template('home.html')



@app.route('/esercizio1',methods = ["GET"])
def esercizio1():
   global provinciaInput
   provinciaInput = request.args.get('provinciaInput')
   prov = provincie3857[provincie3857["DEN_UTS"]== provinciaInput]
   ax = prov.plot(edgecolor =  "red", facecolor = "None",figsize=(12,6),markersize = 5)
   contextily.add_basemap(ax)
   dir = "static/images"
   file_name = "graf1.png"
   save_path = os.path.join(dir, file_name)
   plt.savefig(save_path, dpi = 150)
   return render_template('esercizio1.html')

@app.route('/esercizio2',methods = ["GET"])
def esercizio2():
   prov = provincie3857[provincie3857["DEN_UTS"]== provinciaInput]
   table = comuni3857[comuni3857.within(prov.geometry.item())]
   tabella = table.to_html()
   return render_template('esercizio2.html', tabella = tabella)


@app.route('/esercizio4',methods = ["GET"])
def esercizio4():
   prov = provincie3857[provincie3857["DEN_UTS"]== provinciaInput]
   comuni_provinciaselezionata = comuni3857[comuni3857.within(prov.geometry.item())]
   table = dict(zip(comuni_provinciaselezionata["COMUNE"], comuni_provinciaselezionata["Shape_Area"]))
   return render_template('esercizio4.html', tabella = table)


@app.route('/esercizio5',methods = ["GET"])
def esercizio5():
   def conversione(kmq):
      miglia = kmq * 0.386102
      return miglia
   valore = conversione(45)   
   return render_template('esercizio5.html',valore = valore)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)