#Exercice 7.7
#Question 1
def intersection_2_listes(l1: List[int], l2: List[int]) -> List[int]:
    """Précondition: l1 et l2 deux listes d'éntiers naturels triées
    d'ordre croissant.
    Retourne l'intersection des deux listes.
    """
    l: List[int] = []
    i: int = 0
    n: int = 0
    while i < len(l1) and n < len(l2):
        if l1[i] == l2[n]:
            l.append(l1[i])
            n = n + 1
            i = i + 1
        elif l1[i] < l2[n]:
            i = i + 1
        else:
            n = n + 1
    return l

#Jeu de test
assert intersection_2_listes([0,1,2], [3,4,5]) == []
assert intersection_2_listes([1,2,3],[1,2,3]) == [1, 2, 3]
assert intersection_2_listes([1,1],[1,2]) == [1]
assert intersection_2_listes([],[1,2,3]) ==  []
assert intersection_2_listes([1,2,2,3,4],[2,3,4,4,5,6]) == [2, 3, 4]
assert intersection_2_listes([1,1],[1,1]) == [1, 1]

#Question 2
def intersection(l1: List[List[int]]) -> List[int]:
    """Précondition:
    Retourne l'intersection de toute les listes.
    """
    l: List[int] = intersection_2_listes(l1[0], l1[1])
    i: int
    for i in range(1, len(l1) - 1):
        l = intersection_2_listes(l, l1[i])
    return l

#Jeu de test
assert intersection([[1, 2, 3, 4, 4, 5], [2, 5, 7], [0, 2, 2, 4, 4, 5, 9]]) == [2, 5]
assert intersection([[1, 2, 3, 4, 4, 5], [2, 4, 4, 5, 7], [0, 2, 2, 4, 4, 5, 9]]) == [2, 4, 4, 5]
