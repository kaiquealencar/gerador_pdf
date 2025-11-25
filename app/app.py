from flask import Flask, render_template, request, redirect, url_for, session, send_file
from app.gerar_pdf import gerar_holerite
import os

app = Flask(__name__)
app.secret_key = "86de935e75aaf84e5199eacc2008ab2cbb32b362df82654d5c9c8a0317c81715"  


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == "admin" and senha == "admin123456789":
            session["usuario"] = usuario
            return redirect(url_for("home"))
        else:
            return render_template("login.html", erro="Usuário ou senha incorretos!")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

def login_requerido(func):
    def wrapper(*args, **kwargs):
        if "usuario" not in session:
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


@app.route("/", methods=["GET"])
@login_requerido
def home():
    return render_template("index.html")


@app.route("/gerar-pdf", methods=["POST"])
@login_requerido
def gerar_pdf():
    nome = request.form.get("nome")
    reg_sistema = request.form.get("reg-sis")
    rg = request.form.get("rg")
    cpf = request.form.get("cpf")
    conta = request.form.get("conta")

    caminho_pdf = gerar_holerite(nome, reg_sistema, rg, cpf, conta)

    return send_file(
        caminho_pdf,
        as_attachment=True,
        download_name=os.path.basename(caminho_pdf)
    )
if __name__ == "__main__":
    if not os.environ.get("RENDER"):
        app.run(debug=True)