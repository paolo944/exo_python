from math import pi

"""Donner une définition ainsi qu’un jeu de tests de la fonction aire_disque qui calcule l’aire πr2
d’un disque de rayon r
"""


def aire_disque(r: float) -> float:
    return pi * r * r


assert aire_disque(5) == pi * 25
assert aire_disque(9) == pi * 81
assert aire_disque(4) == pi * 16

"""Donner une définition ainsi qu’un jeu de tests de la fonction aire_couronne qui, étant donné
deux nombres r1 et r2, calcule l’aire de la couronne de rayon intérieur r1 et de rayon extérieur
r2.
Par hypothèse, on considère que le rayon intérieur est inférieur ou égal au rayon extérieur.
"""


def aire_couronne(r1: float, r2: float) -> float:
    return pi * (r2 * r2 - r1 * r1)

"""assert aire_couronne() ==
assert aire_couronne() ==
assert aire_couronne() =="""
