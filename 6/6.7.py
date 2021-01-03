#Exercice 6.7
#Question 1
def liste_mult(L: List[int], k: int) -> List[int]:
    """Précondition: éléments de L et k entier non nul.
    Retourne une liste des éléments de L tous multiplié par k."""
    lr: List[int] = []
    i: int
    for i in L:
        lr.append(i * k)
    return lr

assert liste_mult([3, 5, 9, 4], 2) == [6, 10, 18, 8]
assert liste_mult([], 2) == []
assert liste_mult([2, 5, 10, 20], 5) == [10, 25, 50, 100]

#Question 2
def list_div(L: List[int], k: int) -> List[int]:
    """Précondition: éléments de L et k entier non nul.
    Retourne une liste des éléments de L tous qui sont divisibles par k et les divise pa
    k."""
    lr: List[int] = []
    i: int
    for i in L:
        if i % k == 0:
            lr.append(i // k)
    return lr

#Jeu de test
assert list_div([2, 7, 9, 24, 6], 2) == [1, 12, 3]
assert list_div([2, 7, 9, 24, 6], 3) == [3, 8, 2]
assert list_div([2, 7, 9, 24, 6], 5) == []
assert list_div([2, 7, 9, -24, 6], -3) == [-3, 8, -2]
assert list_div([], 3) == []
