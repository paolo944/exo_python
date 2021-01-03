"""Question 1
Donner une définition de la fonction moyenne_trois_nb qui effectue la moyenne arithmétique
de trois nombres.
Dans le jeu de tests, on vérifiera notamment le calcul de moyenne des nombres 3, 6 et −3 puis
de −3, 0 et 3 puis de 1.5, 2.5 et 1.0 (on pourra ajouter d’autres tests en complément).
"""


def moyenne_trois_nb(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


assert moyenne_trois_nb(3, 6, -3) == 2
assert moyenne_trois_nb(-3, 0, 3) == 0
assert moyenne_trois_nb(1.5, 2.5, 1.0) == 5 / 3

"""Écrire une définition de la fonction moyenne_ponderee qui effectue la moyenne de trois nombres
a, b, c avec des coefficients de pondération, respectivement pa (pondération en a), pb et pc.
Proposer un jeu de tests comprenant au moins trois tests.
"""


def moyenne_ponderee(pa: float, pb: float, pc: float, a: float, b: float, c: float) -> float:
    return (pa * a + pb * b + pc * c) / (pa + pb + pc)

assert moyenne_ponderee(3, 2, 1, 13, 12, 15) == 13
assert moyenne_ponderee(5, 9, 14, 20, 14, 12) == 394/28
assert moyenne_ponderee(2, 3, 3, 1, 18, 15) == 101/8
