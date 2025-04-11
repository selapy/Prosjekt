# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 18:14:53 2025
"""
# =============================================================================
# Supportvaktene i MORSE er delt inn i 2-timers bolker: kl 08-10, kl 10-12, kl 12-14 og kl 14-16. 
# Skriv et program som finner det totale antall henvendelser supportavdelingen mottok for hver av tidsrommene 08-10, 10-12, 12-14 og 14-16 for uke 24. 
# Resultatet visualiseres ved bruk av et sektordiagram (kakediagram).
# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt

# Les Excel-filen
morse = pd.read_excel('support_uke_24 (2).xlsx', sheet_name='Ark1')
print(morse)

# Konverter klokkeslett til time
morse['Klokkeslett'] = pd.to_datetime(morse['Klokkeslett'])


# Funksjon som leggert til klokkeslett i timers bolkers
def Klokkeslett_intervall(time):
    if int(time.strftime('%H')) < 10:
        return '08-10'
    elif int(time.strftime('%H')) < 12:
        return '10-12'
    elif int(time.strftime('%H')) < 14:
        return '12-14'
    elif int(time.strftime('%H')) < 16:
        return '14-16'
    else:
        return 'ingen er tilgjengelig'
#lage en kolonne med tids interval og vis feltene til kolonnene og noen data med interval kolonnen

morse['Tidsintervall'] = morse['Klokkeslett'].apply(Klokkeslett_intervall)

print(morse.columns)
print(morse.head()) 

#count antall hendvendelser per tidsinterval

antall_per_intervall = morse['Tidsintervall'].value_counts(['08-10', '10-12', '12-14', '14-16', 'ingen er tilgjengelig']) 

# Visualiser med kakediagram
antall_per_intervall.plot(kind='pie', color='red')
plt.title('antall henvendelser supportavdelingen mottok for hver av tidsrommene')
plt.show()
