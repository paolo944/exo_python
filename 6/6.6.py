#Exercice 6.6
import math
#Question 1
def somme(L: List[float]) -> float:
    """Précondition: type de L List[float]
    Renvoie la somme des éléments de L ou 0 si y 0 élément."""
    s: float = 0
    i: float
    if len(L) == 0:
        return s
    else:
        for i in L:
            s = s + i
        return s

#Jeu de test
assert somme([1, 2, 3, 4, 5]) == 15
assert somme([1, 2.5, 3.2, 4, 5]) == 15.7
assert somme([1, 2.5, 3.5, 4, 5]) == 16
assert somme([]) == 0

#Question 2
def moyenne(L: List[float]) -> float:
    """Précondition: len(L) > 0 et type(L) == List[float]
    Retourne la moyenne de la liste L."""
    return somme(L) / len(L)

#Jeu de test
assert moyenne([1, 2, 3, 4, 5]) == 3
assert moyenne([1, 2.5, 3.5, 4, 5]) == 3.2
assert moyenne([5]) == 5

#Question 3
def carres(L: List[float]) -> List[float]:
    """Précondition: type(L) == List[float]
    Retourne liste avec le carre de chaque élément de L."""
    lr: List[float] = []
    i: float
    if len(L) == 0:
        return []
    else:
        for i in L:
            lr.append(i**2)
        return lr

#Jeu de test
assert carres([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert carres([-5, -1, 2]) == [25, 1, 4]
assert carres([]) == []
assert carres([10, 0.5]) == [100, 0.25]

#Question 4
def variance(L: List[float]) -> float:
    """Précondition: len(L) > 0 et type(L) == List[float]
    Retourne la variance de L."""
    return moyenne(carres(L)) - ((moyenne(L)) ** 2)

#Jeu de test
assert variance([20, 0, 20, 0]) == 100
assert variance([10, 10, 10, 10]) == 0

#Question 5
def ecart_type(L: List[float]) -> float:
    """Précondition: len(L) > 0 et type(L) == List[float]
    Retourne l'écart-type de la liste L."""
    return math.sqrt(variance(L))

#Jeu de test
assert ecart_type([10, 10, 10, 10]) == 0
assert ecart_type([20, 0, 20, 0]) == 10
assert ecart_type([15, 15, 5, 5]) == 5
assert ecart_type([12, 11, 10, 12, 11]) == 0.7483314773547993
