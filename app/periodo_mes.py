from datetime import date
import calendar

hoje = date.today()

def periodo_mes(mes_corrente):
    primeiro_dia = hoje.replace(day=1)
    ultimo_dia_num = calendar.monthrange(hoje.year, mes_corrente)[1]
    ultimo_dia = date(hoje.year, hoje.month, ultimo_dia_num)
    
    return f"{ primeiro_dia.strftime("%d/%m/%Y") } A { ultimo_dia.strftime("%d/%m/%Y") }"


