"""Bloc Mesurer. Zipf et Heaps sur un vrai corpus de code.

Le corpus de la séance est la bibliothèque standard de Python, déjà présente
sur chaque machine. Dans l'entreprise, DOSSIER devient le dépôt interne.
"""
import os
import pathlib
import re

from texte import lire, reparer, normaliser, tokeniser, mesurer

DOSSIER = pathlib.Path(os.__file__).parent          # la bibliothèque standard, OS module intermediaire f python ayrjj3li texte mais jai besoin de path dakshi bash an appliquer elih pathlib.
#os est le module Python qui gère les fichiers et le système.
mots = []
for fichier in sorted(DOSSIER.glob("*.py")): #glob katqol chercher en fonction de module li an3tik"*.py"
    tokens = tokeniser(normaliser(reparer(lire(fichier))))
    mots += [t for t in tokens if re.fullmatch(r"\w+", t)]   # les mots seuls pas de points de ponctuation

# ---- Zipf, la fréquence selon le rang ----
classement = mesurer(mots).most_common() #DONNE UNE LISTE  triée de tuples (mot, fréquence), du plus fréquent au moins fréquent.
print("rang  token        fréquence  rang x fréquence")
for rang in (1, 2, 3, 10, 100):
    token, f = classement[rang - 1]
    print(f"{rang:<5} {token:<12} {f:<10} {rang * f}")

# ---- Heaps, le vocabulaire selon le nombre de mots lus ----
vus = set()
print("\nmots lus N   vocabulaire V")
for n, mot in enumerate(mots, start=1):
    vus.add(mot)
    if n in (1_000, 10_000, 100_000) or n == len(mots): #N HIA SHHAL MN MOT QRA lhd l 2an , len(mots) shhal mn mra ban
        print(f"{n:<12} {len(vus)}")
