#Exercice 8.4
#Question 1:
def moyenne(l: List[float]) -> float:
    """Précondition: len(n) > 0.
    Retourne la moyenne de la liste l.
    """
    s: float = 0
    i : float
    for i in l:
        s = s + i
    return s / len(l)

#Jeu de test
assert moyenne([10,10,10]) == 10
assert moyenne([0,10,20]) == 10
assert moyenne([1,2]) == 1.5

#Question 2
def ecart_nombre(l: List[float], x: float) -> List[float]:
    """Précondition: len(l) > 0
    Retourne la valeur absolue de la différences des nombres de l avec
    x.
    """
    return [abs(n - x) for n in l]

#Jeu de test
assert ecart_nombre([10,10,10],10) == [0, 0, 0]
assert ecart_nombre([0,10,20], 10) == [10, 0, 10]
assert ecart_nombre([1,2],1.5) == [0.5, 0.5]

#Question 3
def liste_carre(l: List[float]) -> List[float]:
    """Précondition: aucune
    Retourne la liste des nombres dans l au carré.
    """
    return [i*i for i in l]

#Jeu de test
assert liste_carre([0,0,0]) == [0, 0, 0]
assert liste_carre([10,0,10]) == [100, 0, 100]
assert  liste_carre([0.5,0.5]) == [0.25, 0.25]

#Question 4
def variance(l: List[float]) -> float:
    """Précondition: aucune
    Renvoie la variance de la liste l.
    """
    return moyenne(liste_carre(ecart_nombre(l, moyenne(l))))

#Jeu de test
assert variance([10,10,10]) == 0.0
assert variance([0,10,20]) == 66.66666666666667
assert variance([1,2]) == 0.25

#Question 5
def variance_bis(l : List[float]) -> float:
    """Précondition: aucune
    Retourne la variance associée à l.
    """
    m: float = moyenne(l)
    lv: List[float]
    lv = [abs(m-i)**2 for i in l]
    return moyenne(lv)

#Jeu de test
assert variance_bis([10,10,10]) == 0.0
assert variance_bis([0,10,20]) == 66.66666666666667
assert variance_bis([1,2]) == 0.25
