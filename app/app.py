from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
from app.gerar_pdf import gerar_holerite
import os

app = Flask(__name__)
app.secret_key = "86de935e75aaf84e5199eacc2008ab2cbb32b362df82654d5c9c8a0317c81715"

USUARIO = "admin"
SENHA = "@dmin1234@"



@app.route("/")
def index():
    session.pop("logado", None)
    if session.get("logado"):
        return redirect(url_for("home"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == USUARIO and senha == SENHA:
            session["logado"] = True  
            return redirect(url_for("home"))
        else:
            erro = "Usuário ou senha incorretos"
            return render_template("login.html", erro=erro)

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("logado", None)
    return redirect(url_for("login"))


@app.route("/home")
def home():
    if not session.get("logado"):
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/gerar-pdf", methods=["POST"])
def gerar_pdf():
    if not session.get("logado"):
        return redirect(url_for("login"))

    nome = request.form.get("nome", "").upper()
    reg_sistema = request.form.get("reg-sis")
    rg = request.form.get("rg")
    cpf = request.form.get("cpf")
    conta = request.form.get("conta")
    mes_referencia = request.form.get("meses") 


    caminho_pdf = gerar_holerite(nome, reg_sistema, rg, cpf, conta, mes_referencia)

    return send_file(
        caminho_pdf,
        as_attachment=True,
        download_name=os.path.basename(caminho_pdf)
    )



if __name__ == "__main__":
    if not os.environ.get("RENDER"):
        app.run(debug=True)
