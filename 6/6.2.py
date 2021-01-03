#Exercice 6.2
#Question 1
def max_liste(l: List[float]) -> float:
    """Précondition: len(l) > 0
    Retourne le plus grande élément de la liste l."""
    max_n: float = l[0]
    i: float
    for i in l[1:]:
        if i > max_n:
            max_n = i
    return max_n

#Jeu de test
assert max_liste([3, 7, 9, 5.4, 8.9, 9, 8.999, 5]) == 9
assert max_liste([5,6,5,4,12,200]) == 200
assert max_liste([6,100, 200, 500]) == 500

#Question 2
def nb_occurrences(L: List[T], x: T) -> int:
    """Précondition: aucune
    Retourne le nombre d'occurence de x dans L"""
    i: T
    compteur: int = 0
    for i in L:
        if i == x:
            compteur = compteur + 1
    return compteur

#Jeu de test
assert nb_occurrences([3, 7, 9, 5.4, 8.9, 9, 8.999, 5], 9) == 2
assert  nb_occurrences(["chat", "ours", "chat", "chat", "loup"], "chat") == 3
assert nb_occurrences(["chat", "ours", "chat", "chat", "loup"], "ou") == 0

#Question 3
def nb_max(L: List[float]) -> int:
    """Précondition: len(L) > 0
    Retourne le nombre d'occurence du maximum de L dans L."""
    return nb_occurrences(L, max_liste(L))

#Jeu de test
assert nb_max([3, 7, 9, 5.4, 8.9, 9, 8.999, 5]) == 2
assert nb_max([-2, -1, -5, -3, -1, -4, -1]) == 3
