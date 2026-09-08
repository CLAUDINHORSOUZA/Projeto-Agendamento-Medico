from flask import Flask, render_template
from controllers import medico_controller

import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="290380",
    database="agendamento_medico",
   
)

#rota para a pagina principal
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/medico", methods=["GET", "POST"])
def medico():
	return medico_controller.cadastrar_medico()


if __name__ == '__main__':
    app.run(debug=True) 