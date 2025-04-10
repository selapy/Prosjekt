# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 17:51:11 2025

"""
# =============================================================================
# KREVENDE: Skriv et program som regner ut gjennomsnittlig samtaletid basert på alle henvendelser i uke 24.
# =============================================================================

import pandas as pd


# Les Excel-filen fra mappen hvor jeg har skriptet og print kolonnenavn
morse = pd.read_excel('support_uke_24 (2).xlsx', sheet_name='Ark1')

# Hent ut kolonnen med samtaletid (varighet)
varighet = morse['Varighet'].array

# Funksjon for å konvertere hh:mm:ss til sekunder
def get_seconds(Varighet):
    hh, mm, ss = Varighet.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)

# Lag liste med antall sekunder for hver varighet
sekunder_liste = [get_seconds(tid) for tid in varighet]

# Beregn gjennomsnitt
gjennomsnitt_sekunder = sum(sekunder_liste) / len(sekunder_liste)
    
print('Gjennomsnitt i sekunder:', gjennomsnitt_sekunder)

# Konverter tilbake til hh:mm:ss
timer = int(gjennomsnitt_sekunder // 3600)
minutter = int((gjennomsnitt_sekunder % 3600) // 60)
sekunder = int(gjennomsnitt_sekunder % 60)

print(timer,":", minutter,":", sekunder, "er gjennomsnittlig samtaletid basert på alle henvendelser i uke 24")