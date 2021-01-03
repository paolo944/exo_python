"""Une association propose des excursions à la journée. Ses frais incluent :
— le transport en autocars de 60 places, facturé 1200 euros la journée par autocar.
— le salaire de guides touristiques, à raison d’un guide pour 18 personnes maximum, facturé
300 euros la journée par guide.
Donner la définition et un jeu de tests de la fonction excursion qui étant donné un entier
nb_pers calcule le coût (minimum) pour l’association d’une excursion de nb_pers personnes.
Remarque: Tout autocar contenant au moins une personne (de même, tout guide affecté à au
moins une personne) doit être payé en totalité.
"""


def excursion(nb_personnes: int) -> int :
