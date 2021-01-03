#Exercice 7.8
CarreMagique : List[List[int]]
CarreMagique = [ [2, 7, 6],
[9, 5, 1],
[4, 3, 8] ]

#Question 1
def presence(n: int, l: List[int]) -> bool:
    """Précondition: aucune
    Renvoie True si n est contenu dans l sinon renvoie False.
    """
    i: int
    for i in l:
        if i == n:
            return True
    return False

#Jeu de test
assert presence(5, [9, 5, 1]) == True
assert presence(4, [9, 5, 1]) == False

#Question 2
def mat_presence(n: int, l1: List[List[int]]) -> bool:
    """Précondition: aucune
    Renvoie True si n est contenu dans l1 sinon renvoie False.
    """
    l: List[int]
    for l in l1:
        if presence(n, l) == True:
            return True
    return False

#Jeu d test
assert mat_presence(5, [[1, 2, 3], [4, 5, 6]]) == True
assert mat_presence(7, [[1, 2, 3], [4, 5, 6]]) == False
assert mat_presence(7, CarreMagique) == True

#Question 3
def verif_elems(n: int, l1: List[List[int]]) -> bool:
    """Précondition: aucune.
    Renvoie True si tous les éléments de 1 à n*n sont contenu dans l1
    renvoie False sinon.
    """
    i: int
    for i in range(1, n*n+1):
        if mat_presence(i, l1) == False:
            return False
    return True

#Jeu de test
assert verif_elems(3, CarreMagique) == True
assert verif_elems(3, [ [2, 7, 6], [8, 5, 1], [4, 3, 8] ]) == False

#Question 4
def somme_liste(l: List[int]) -> int:
    """Précondition: aucune
    Renvoie la sommme des éléments de la liste.
    """
    s: int = 0
    i: int
    for i in l:
        s = s + i
    return s

#Jeu de test
assert somme_liste([2, 7, 6]) == 15
assert somme_liste([9, 5, 1]) == 15
assert somme_liste([4, 3, 8]) == 15

#Question 5
def verif_lignes(l1: List[List[int]], s: int) -> bool:
    """Précondition: aucune
    Renvoie True si toutes les lignes ont la même somme de ligne
    sinon renvoie False.
    """
    l: List[int]
    for l in l1:
        if somme_liste(l) != s:
            return False
    return True

#Jeu de test
assert verif_lignes(CarreMagique, 15) == True
assert verif_lignes(CarreMagique, 16) == False
assert verif_lignes([ [2, 7, 6], [8, 5, 1], [4, 3, 8] ], 15) == False

#Question 6
def colonne(j: int, l1: List[List[int]]) -> List[int]:
    """Précondition: aucune
    Renvoie la colone j demandé.
    """
    l_j: List[int] = []
    l: List[int]
    for l in l1:
        l_j.append(l[j])
    return l_j

#Jeu de test
assert colonne(0, [ [2, 7, 6],
[9, 5, 1],
[4, 3, 8] ]) == [2, 9, 4]
assert colonne(1, [ [2, 7, 6],
[9, 5, 1],
[4, 3, 8] ]) == [7, 5, 3]
assert colonne(2, [ [2, 7, 6],
[9, 5, 1],
[4, 3, 8] ]) ==[6, 1, 8]
