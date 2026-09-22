from flask import request, render_template
import app




def cadastrar_procedimento():
    if request.method == "POST":
        nome = request.form["nome"].upper()
        duracao = request.form["duracao"]
        data = request.form["data"]

        cursor = app.db.cursor()
        cursor.execute("INSERT INTO procedimento (nome, duracao, data) VALUES (%s, %s, %s)",
                       (nome, duracao, data))
        app.db.commit()

        return render_template("confirmar_procedimento.html", nome=nome, duracao=duracao, data=data)
    return render_template("cadastrar_procedimento.html")