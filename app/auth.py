from flask import session, flash, get_flashed_messages

USUARIO = "admin"
SENHA = "admin@holerite"

def login(usuario, senha):
    if usuario == USUARIO and senha == SENHA:
        session["logado"] = True
        return True
    else:
        flash("Usuário ou senha incorreto!", "error")
        return False
    
