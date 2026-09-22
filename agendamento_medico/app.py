from flask import Flask, render_template
from controllers import medico_controller
from controllers import procedimento_controller

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

@app.route("/procedimento", methods=["GET", "POST"])
def procedimento():
    return procedimento_controller.cadastrar_procedimento()

if __name__ == '__main__':
    app.run(debug=True) 