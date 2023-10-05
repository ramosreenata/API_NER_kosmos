# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:05:08 2023

@author: Renata
"""

from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

nlp = spacy.load('es_core_news_sm')

@app.route('/ner', methods=['POST'])
def recognize_entities():
    try:
        data = request.json
        texto = data['texto']
        doc = nlp(texto)
        entidades = [(ent.text, ent.label_) for ent in doc.ents]
        return jsonify({"entidades": entidades})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
