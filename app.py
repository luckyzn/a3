from flask import Flask, jsonify, request
from sklearn.linear_model import LinearRegression as lr
import pandas as pd
import numpy as np

diagnostico = ["ID"]
colunas = ['eritrocitos','hemoglobina','hematocrito','hcm','vgm','chgm','metarrubricitos','proteina_plasmatica','leucocitos','leucograma','segmentados','bastonetes','blastos','metamielocitos',
          'mielocitos','linfocitos','monocitos','eosinofilos','basofilos','plaquetas']
planilha = pd.read_csv ('dataset-hemograma.csv')
def cria_modelo():
  return lr().fit(planilha[colunas],planilha[diagnostico])

modelo = cria_modelo()

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hemograma():
   
    data = request.json(silent=True)
    #data = request.get_json(silent=True)
    if data is None:
      return jsonify({"error": "Erro aqui"}), 400
    num_eritrocitos = data.get('eritrocitos')
    num_hemoglobina = data.get('hemoglobina')
    num_hematocrito = data.get ('hematocrito')
    num_hcm = data.get('hcm')
    num_vgm = data.get('vgm')
    num_chgm = data.get ('chgm')
    num_metarrubricitos = data.get('metarrubricitos')
    num_proteina = data.get('proteina_plasmatica')
    num_leucocitos = data.get('leucocitos')
    num_leucograma = data.get('leucograma')
    num_segmentados = data.get('segmentados')
    num_bastonetes = data.get ('bastonetes')
    num_blastos = data.get ('blastos')
    num_metamielocitos = data.get('metamielocitos')
    num_mielocitos = data.get('mielocitos')
    num_linfocitos = data.get('liefocitos')
    num_monocitos = data.get('monocitos')
    num_eosinofilos = data.get('eosinofilos')
    num_basofilos = data.get('basofilos')
    num_plaquetas = data.get('plaquetas')
    dadosFinais = np.array([[float(num_eritrocitos),float(num_hemoglobina),float(num_hematocrito),float(num_hcm),float(num_vgm),float(num_chgm),float(num_metarrubricitos),float(num_proteina),float(num_leucocitos),float(num_leucograma),float(num_segmentados),float(num_bastonetes),float(num_blastos),float(num_metamielocitos),
                          float(num_mielocitos),float(num_linfocitos),float(num_monocitos),float(num_eosinofilos),float(num_basofilos),float(num_plaquetas)]])
    resultado = modelo.predict(dadosFinais)[0]
    if resultado == diagnostico[int]:
      return jsonify ({"message":(diagnostico[int])})