# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:21:50 2025

"""
# =============================================================================
# Del a) Skriv et program som leser inn filen ‘support_uke_24.xlsx’ og 
# lagrer data fra kolonne 1 i en array med variablenavn ‘u_dag’, 
# dataen i kolonne 2 lagres i arrayen ‘kl_slett’, data i kolonne 3 lagres i arrayen ‘varighet’ og
# dataen i kolonne 4 lagres i arrayen ‘score’. Merk: filen ‘support_uke_24.xlsx’ må ligge i samme mappe som Python-programmet ditt.
# =============================================================================

import pandas as pd


# Les Excel-filen fra mappen hvor jeg har skriptet og print kolonnenavn
morse = pd.read_excel('support_uke_24 (2).xlsx',sheet_name='Ark1')
print(morse.columns)

# lagrer data som array
u_dag = morse['Ukedag'].array
kl_slett = morse['Klokkeslett'].array
varighet = morse['Varighet'].array
score = morse['Tilfredshet'].array


# Vis alle rader i filen

print("Ukedager:", u_dag)
print("Klokkeslett:", kl_slett)
print("Varighet:", varighet)
print("Score:", score)