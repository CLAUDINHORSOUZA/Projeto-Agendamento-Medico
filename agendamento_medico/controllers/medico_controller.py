from flask import request, render_template

from app import db

def cadastrar_medico():
    if request.method == "POST":
        nome = request.form["nome"].upper()
        crm = request.form["crm"]
        estado = request.form["estado"].upper()
        email = request.form["email"]
        telefone = request.form["telefone"]

        cursor = db.cursor()
        cursor.execute("INSERT INTO medico (nome, crm, estado, email, telefone) VALUES (%s, %s, %s, %s, %s)",
                       (nome, crm, estado, email, telefone))
        db.commit()

        return render_template("confirmar_medico.html", nome=nome, crm=crm, estado=estado, email=email, telefone=telefone)
    return render_template("cadastrar_medico.html")