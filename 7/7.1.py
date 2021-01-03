#Exercice 7.1
#Question 1
Complexe = Tuple[float, float]
def partie_reelle(c: Complexe) -> float:
    """Précondition: Complexe = couple de type float, float.
    Retourne partie réelle du complexe.
    """
    re, _ = c
    return re

def partie_imaginaire(c: Complexe) -> float:
    """Précondition: Complexe = couple de type float, float.
    Retourne partie imaginaire du complexe.
    """
    _, im = c
    return im

#Jeu de test
assert partie_reelle((2.0,3.0)) == 2.0
assert partie_imaginaire((2.0,3.0)) == 3.0
assert partie_reelle((0.0,1.0)) == 0.0
assert partie_imaginaire((0.0,1.0)) == 1.0
assert partie_reelle((4.0,0.0)) == 4.0
assert partie_imaginaire((4.0,0.0)) == 0.0

#Question 2
def addition_complexe(c1: Complexe, c2: Complexe) -> Complexe:
    """Retourne c1 + c2.
    """
    re1, im1 = c1
    re2, im2 = c2
    return (re1 + re2, im1 + im2)

#Jeu de test
assert addition_complexe((1.0, 0.0), (0.0, 1.0)) == (1.0, 1.0)
assert addition_complexe((2.0, 3.0), (0.0, 1.0)) == (2.0, 4.0)

#Question 4
def produit_complexe(c1: Complexe, c2: Complexe) -> Complexe:
    """Retourne le produit de c1 et c2.
    """
    re1, im1 = c1
    re2, im2 = c2
    return ((re1 * re2 - im1 * im2), (re1 * im2 + im1 * re2))

#Jeu de test
assert produit_complexe((0.0, 0.0), (1.0, 1.0)) ==(0.0, 0.0)
assert produit_complexe((0.0, 1.0), (0.0, 1.0)) == (-1.0, 0.0)
assert produit_complexe((2.0, 3.0), (0.0, 1.0)) == (-3.0, 2.0)
