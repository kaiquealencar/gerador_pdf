#from datetime import date, timedelta
#import calendar

import datetime
import calendar

def quinto_dia_util(ano, mes):
    dias_uteis_encontrados = 0
    data = datetime.date(ano, mes, 1) 
    
    while True:
        if data.weekday() < 5: 
            dias_uteis_encontrados += 1
            if dias_uteis_encontrados == 5:
                return f"{ data.strftime("%d/%m/%Y") }"
        
        data += datetime.timedelta(days=1)
        
        if data.month != mes:
            return None


