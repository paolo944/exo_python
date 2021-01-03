# Exercice 6.8
# Question 1
def entrelacement(l1: List[T], l2: List[T]) -> List[T]:
    """Précondition: l1 et l2 de même type et même longeur.
    Renvoie l'entrelacement de ces 2 listes."""
    lr: List[T] = []
    i: int = 0
    while i < len(l1) and i < len(l2):
        lr.append(l1[i])
        lr.append(l2[i])
        i = i + 1
    return lr


# Jeu de test
assert entrelacement([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
assert entrelacement([2, 5, 8, 10], [3, 20, 40, 5]) == [2, 3, 5, 20, 8, 40, 10, 5]
assert entrelacement([], []) == []


# Question 2
def entrelacement_general(l1: List[T], l2: List[T]) -> List[T]:
    """Précondition: l1 et l2 de même type.
    Renvoie une liste obtenu en intercalant l1 et l2."""
    if len(l1) == len(l2):
        return entrelacement(l1, l2)
    else:
        if len(l1) > len(l2):
            return entrelacement(l1[:len(l2)], l2) + l1[len(l2):]
        else:
            return entrelacement(l1, l2[:len(l1)]) + l2[len(l1):]

# Jeu de test
assert entrelacement_general([1, 2, 3], [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
assert entrelacement_general([1, 2, 3], [4, 5, 6, 7, 8]) == [1, 4, 2, 5, 3, 6, 7, 8]
assert entrelacement_general([1, 2, 3, 4, 5], [6, 7, 8]) == [1, 6, 2, 7, 3, 8, 4, 5]
