import os
import csv
from flask import Flask, render_template

app = Flask(__name__)

# Definindo ambiente para modo de desenvolvimento (debug)
os.environ['FLASK_DEBUG'] = 'True'
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/glossario')
def glossario():

    glossario_de_termos = []

    with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            glossario_de_termos.append(linha)

    return render_template(
        "glossario.html",
        glossario=glossario_de_termos)


if __name__ == '__main__':
    app.run()
