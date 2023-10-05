# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:05:08 2023

@author: Renata
"""

from flask import Flask, request, jsonify
import spacy


app = Flask(__name__)

# Descargamos el modelo en español
nlp = spacy.load('es_core_news_sm') 

# Especificamos que es un POST request y añadimos /ner al URL
@app.route('/ner', methods=['POST'])

def recognize_entities():
    try:
        # Hacemos el request de la data
        data = request.json
        oraciones = data['oraciones']
        results = []

        for oracion in oraciones:
            doc = nlp(oracion)
            # Extraemos las entidades
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            # Juntamos la oración con el resultado
            results.append({"oración": oracion, "entidades": entities})

        return jsonify({"resultado": results})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
