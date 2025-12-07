import os

from flask import Flask, render_template, redirect, session, send_file, flash, request, url_for

from listas.escolas import escolas
from gerar_holerite import GerarHolerite
from auth import login

app = Flask(__name__)
app.secret_key = "d2e90a70c44d53aae0f1284548aa62a08a9fa786d28fbfb5c0a6c6ea4163acbe"

@app.route("/login", methods=["GET", "POST"])
def rota_login():
    if request.method == "POST":
        usuario, senha = request.form.get("usuario"), request.form.get("senha")
        if login(usuario, senha):
            session["logado"] = True
            session["usuario"] = usuario
            return render_template("index.html", escolas=escolas)
    return render_template("login.html")
        

@app.route("/logout", methods=["GET", "POST"])
def rota_logout():
    session.clear()
    return redirect(url_for("rota_login"))


@app.route("/")
def index():
    if not session.get("logado"):
        return redirect(url_for("rota_login"))
    
    return render_template('index.html', escolas=escolas)

@app.route("/gerar-pdf", methods=["GET", "POST"])
def gerar_pdf():
    if not session.get("logado"):
        return redirect(url_for("rota_login"))
    
    if request.method == "POST":
        gera_holerite = GerarHolerite()

        nome = request.form.get("nome")
        reg_sis = request.form.get("reg-sis")
        rg = request.form.get("rg")
        cpf = request.form.get("cpf")
        conta = request.form.get("conta")
        mes_referencia = request.form.get("meses")
        escola  = request.form.get("escola")
        path_pdf= gera_holerite.gerar_holerite(nome, reg_sis, rg, cpf, conta, mes_referencia, escola)
        return send_file(
            path_pdf,
            as_attachment= True,
            download_name= os.path.basename(path_pdf)
        )
    
    




if __name__ == "__main__":
    app.run(debug=True)