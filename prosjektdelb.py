# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 00:42:52 2025
# =============================================================================
# Skriv et program som finner antall henvendelser for hver de 5 ukedagene. 
# Resultatet visualiseres ved bruk av et søylediagram (stolpediagram).
# =============================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt

# Les Excel-filen fra mappen hvor jeg har skriptet og print kolonnenavn
morse = pd.read_excel('support_uke_24 (2).xlsx',sheet_name='Ark1')

# Hent ukedager
udag = morse['Ukedag'].array

# Beregne henvendelser per ukedag
henvendelser_per_dag = morse['Ukedag'].value_counts()
print(henvendelser_per_dag)

# visualiseres ved bruk av et søylediagram (stolpediagram)
henvendelser_per_dag.plot(kind='bar', color='red')
plt.xlabel("ukedager")
plt.ylabel("henvendelser")
plt.title("antall henvendelser for hver de 5 ukedagene")
plt.show()