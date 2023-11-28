from flask import Flask, jsonify, request
from sklearn.linear_model import LinearRegression as lr
import pandas as pd
import numpy as np

dicionario_doencas = {
   1: "DRC",
   2: "Hipercolesterolemia",
   3:"Anemia",
   4:"Lesao Hepatica",
   5:"Infeccao Bacteriana",
   6:"Desidratação",
   7:"Infecccao Parasitaria",
   8:"Infeccao Viral",
   9:"DRC e Cardiopatia",
   10:"Neoplasia Hepatica",
   11:"Anemia Hemolitica",
   12:"Diabetes",
   13:"Pre-Diabetes",
   14:"Anemia e Infeccao",
   15:"Hepatopata",
   16:"Trombocitopenia e Inflamacao",
   17:"Hipoblasia Mieloide",
   18:"Pancreatite",
   19:"Inflamacao Grave"
}
diagnostico = ["ID"]
colunas = ["eritrocitos","hemoglobina","hematocrito","hcm","vgm","chgm","metarrubricitos",
    "proteina_plasmatica","leucocitos","leucograma","segmentados","bastonetes","blastos","metamielocitos",
    "mielocitos","linfocitos","monocitos","eosinofilos","basofilos","plaquetas"]
planilha = pd.read_csv ('dataset-hemograma.csv')
def cria_modelo():
  return lr().fit(planilha[colunas],planilha["ID"])

modelo = cria_modelo()

app = Flask(__name__)

@app.route("/hemograma", methods=['POST'])
def hemograma():
    print(request)
    data = request.json
    if data is None:
      return jsonify({"error": "Erro aqui"}), 400
    num_eritrocitos = data['eritrocitos']
    num_hemoglobina = data['hemoglobina']
    num_hematocrito = data['hematocrito']
    num_hcm = data['hcm']
    num_vgm = data['vgm']
    num_chgm = data['chgm']
    num_metarrubricitos = data['metarrubricitos']
    num_proteina = data['proteina_plasmatica']
    num_leucocitos = data['leucocitos']
    num_leucograma = data['leucograma']
    num_segmentados = data['segmentados']
    num_bastonetes = data['bastonetes']
    num_blastos = data['blastos']
    num_metamielocitos = data['metamielocitos']
    num_mielocitos = data['mielocitos']
    num_linfocitos = data['linfocitos']
    num_monocitos = data['monocitos']
    num_eosinofilos = data['eosinofilos']
    num_basofilos = data['basofilos']
    num_plaquetas = data['plaquetas']

    dadosFinais = np.array([[num_eritrocitos,num_hemoglobina,num_hematocrito,num_hcm,num_vgm,
        num_chgm,num_metarrubricitos,num_proteina,num_leucocitos,num_leucograma,num_segmentados,
        num_bastonetes,num_blastos,num_metamielocitos,
        num_mielocitos,num_linfocitos,num_monocitos,num_eosinofilos,num_basofilos,num_plaquetas]])
    resultado = modelo.predict(dadosFinais)[0]
    print(dadosFinais)
    retorno = int(resultado)
    return jsonify ({"message":(dicionario_doencas[retorno])})

app.run()