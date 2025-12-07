import os
from datetime import date, datetime, timedelta
from calendar import calendar, monthrange

import fitz


class GerarHolerite:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PDF_BASE = os.path.join(
            BASE_DIR,
            "modelo",
            "holerite.pdf"
        )    

    def __init__(self):
        self.pdf = fitz.open(self.PDF_BASE)
        self.page = self.pdf[0]


    def escrever(self, texto, x, y, tamanho=8, bold=False):
        fonte = "helv" if not bold else "helv-bold"
        self.page.insert_text((x, y), texto, fontsize=  tamanho, fontname=fonte)

  
    def quinto_dia_util(self, ano, mes):
        dias_uteis_encontrados = 0
        data = date(ano, mes, 1) 
    
        while True:
            if data.weekday() < 5: 
                dias_uteis_encontrados += 1
                if dias_uteis_encontrados == 5:
                    return f"{ data.strftime("%d/%m/%Y") }"

            data += timedelta(days=1)

            if data.month != mes:
                return None

    @staticmethod
    @staticmethod
    def periodo_mes(mes_referencia: int):
        ano_atual = date.today().year
    
        if mes_referencia == 1:
            primeiro_dia = date(ano_atual, 12, 1)
            ultimo_dia = date(ano_atual, 12, monthrange(ano_atual, 12)[1])
        else:
            primeiro_dia = date(ano_atual, mes_referencia - 1, 1)
            ultimo_dia = date(ano_atual, mes_referencia - 1, monthrange(ano_atual, mes_referencia - 1)[1])
    
            return f"{primeiro_dia.strftime('%d/%m/%Y')} A {ultimo_dia.strftime('%d/%m/%Y')}"

    def escrever_periodo(self, mes_referencia):
        linha = 302
        for i in range(10):   
            self.escrever(self.periodo_mes(int(mes_referencia)), 380, linha) 
            linha += 12

    def gerar_holerite(self, nome, reg_sistema, reg_geral, cpf, conta, mes_referencia, escola):
        ano = datetime.now().year
        mes = int(mes_referencia)

        self.escrever(nome,        73, 148.5)
        self.escrever(reg_sistema, 248, 148.5)
        self.escrever(reg_geral,   378, 148.5)
        self.escrever(cpf,         455, 148.5)
        self.escrever(conta,   378, 248)
        self.escrever(str(self.quinto_dia_util(ano, mes)), 418, 273)
        self.escrever(escola, 239, 225)
        self.escrever_periodo(mes_referencia)     
        self.escrever(datetime.now().strftime("%d/%m/%Y"), 280, 605)

        output = os.path.join(self.BASE_DIR, f"holerite_{mes_referencia.split()[0]}_{nome.split()[0]}.pdf")
        self.pdf.save(output)
        self.pdf.close()

        return output
