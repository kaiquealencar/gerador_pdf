from datetime import date
import calendar
hoje = date.today()




def periodo_mes(mes_referencia: int):
    
    if mes_referencia == 1:
        primeiro_dia = date(date.today().year, 12, 1)
        ultimo_dia = date(date.today().year, 12, calendar.monthrange(date.today().year, 12)[1])        
    else:
        primeiro_dia = date(date.today().year, mes_referencia -1, 1)
        ultimo_dia = date(date.today().year, mes_referencia -1, calendar.monthrange(date.today().year, mes_referencia -1)[1]) 
    
    return f"{ primeiro_dia.strftime('%d/%m/%Y') } A { ultimo_dia.strftime('%d/%m/%Y') }"

