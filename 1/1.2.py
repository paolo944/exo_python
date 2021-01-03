"""Ecrire une définition de la fonction prix_ttc qui calcule le prix toutes taxes comprises (TTC)
à partir d’un prix hors taxe (HT) et d’un taux de TVA exprimé en pourcentage, par exemple
20.0 pour une TVA de 20%.
"""


def prix_ttc(prix: float, tva: float) -> float:
    return prix * (1 + tva / 100)


assert prix_ttc(100, 20) == 120
assert prix_ttc(100, 0) == 100
assert prix_ttc(100, 100) == 200
assert prix_ttc(0, 20) == 0
assert prix_ttc(200, 5.5) == 211

"""Donner une définition de la fonction prix_ht qui calcule le prix hors taxe à partir du prix toutes
taxes comprises et du taux de TVA.
"""


def prix_ht(prix: float, tva: float) -> float:
    return prix / (1 + tva / 100)

assert prix_ht(120, 20) == 100
assert prix_ht(100, 0) == 100
assert prix_ht(200, 100) == 100
assert prix_ht(0, 20) == 0
assert prix_ht(211, 5.5) == 200