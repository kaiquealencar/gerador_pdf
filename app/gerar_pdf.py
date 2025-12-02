import fitz
import os
from app.pay_day import quinto_dia_util
from app.periodo_mes import periodo_mes
from datetime import date, datetime

now = datetime.now()


def gerar_holerite(nome, reg_sistema, reg_geral, cpf, conta, mes_referencia):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PDF_BASE = os.path.join(BASE_DIR, "modelo.pdf")

    pdf = fitz.open(PDF_BASE)
    page = pdf[0]

    def escrever(texto, x, y, tamanho=7, bold=False):
        fonte = "helv" if not bold else "helv-bold"
        page.insert_text((x, y), texto, fontsize=tamanho, fontname=fonte)

    
    escrever(nome,        73, 148.5)
    escrever(reg_sistema, 248, 148.5)
    escrever(reg_geral,   378, 148.5)
    escrever(cpf,         455, 148.5)
    escrever(conta,   378, 248)
    escrever(str(quinto_dia_util(now.year, int(mes_referencia))), 418, 273)
    
    data_hoje = date.today()
    mes_anterior = data_hoje.month - 1
    
    linha = 302
    for i in range(10):   
        escrever(periodo_mes(int(mes_referencia)), 388, linha) 
        linha += 12
    
    escrever(now.strftime("%d/%m/%Y"), 280, 605)
   

    output = os.path.join(BASE_DIR, f"holerite_{nome.split()[0]}.pdf")
    pdf.save(output)
    pdf.close()

    
    return output
