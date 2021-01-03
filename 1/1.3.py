"""Après avoir spécifié le problème, écrire un jeu de tests et donner une définition de la fonction
polynomiale telle que polynomiale(a, b, c, d, x) évalue le polynôme ax3 + bx2 + cx + d
(à coefficients flottants).
"""


def polynomiale(a: float, b: float, c: float, d: float, x: float) -> float:
    return a * x ** 3 + b * x ** 2 + c * x + d

assert polynomiale(1, 1, 1, 1, 2) == 15
assert polynomiale(1, 1, 1, 1, 3) == 40
assert polynomiale(2, 0, 0, 0, 1) == 2
assert polynomiale(0, 3, 0, 0, 1) == 3
assert polynomiale(0, 0, 4, 0, 1) == 4
assert polynomiale(1, 2, 3, 4, 0) == 4
assert polynomiale(2, 3, 4, 5, 1) == 14

"""Après avoir spécifié le problème, écrire un jeu de tests et donner une définition de la fonction
polynomiale_carre qui rend la valeur de ax4 + bx2 + c.
"""

def polynomiale_carre(a:float, b: float, c:float, x:float) -> float:
    return a * x**4 + b * x**2 + c

assert polynomiale_carre(1, 1, 1, 2) == 21
assert polynomiale_carre(1, 1, 1, 3) == 91