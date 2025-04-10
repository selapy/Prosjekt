# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 17:45:21 2025

@author: 
"""
# =============================================================================
# Skriv et program som finner minste og lengste samtaletid som er loggført for uke 24. 
# Svaret skrives til skjerm med informativ tekst.
# =============================================================================
import pandas as pd

 # Les Excel-filen fra mappen hvor jeg har skriptet og print kolonnenavn
morse = pd.read_excel('support_uke_24 (2).xlsx',sheet_name='Ark1')

# Hente varighet
varighet = morse ['Varighet'].array

# Finner minste og lengste samtaletid som er loggført for uke 24
minste = varighet.min()
lengste = varighet.max()

# Svaret med informativ tekst
print(minste, "er minste samtaletid som er loggført for uke 24 i MORSE")
print(lengste, "er lengste samtaletid som er loggført for uke 24 i MORSE")