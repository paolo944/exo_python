#Exercice 5.1:
#Question 1:
def somme_carres(n: int) -> int:
    """Précondition: n supérieur ou egale à 0 et entier.
    Renvoie la somme des carre inferieurs à n. """
    s: int = 0
    i: int
    for i in range(n+1):
        s = s + i*i
    return s

assert somme_carres(0) == 0
assert somme_carres(2) == 5
assert somme_carres(5) == 55

#Question 2:
def f(m: int, n: int) -> int:
    """Précondition: 0<=m<=n
    Retourne le produit des cubes des entiers dans l'intervalle [m, n[
    """
    p: int = 1
    k: int
    for k in range(m, n):
        p = p * (k**3)

    return p

assert f(1, 4) == 216
assert f(2, 4) == 216
assert f(4, 8) == 592704000
