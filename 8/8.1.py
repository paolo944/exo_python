#Exercice 8.1
#Question 1
def repetition(c: T, n: int) -> List[T]:
    """Précondition: n de type int
    Retourne une liste contenant n fois c.
    """
    return [c for i in range(n)]

#Jeu de test
assert repetition("thon", 4) == ['thon', 'thon', 'thon', 'thon']
assert repetition(3, 8) == [3, 3, 3, 3, 3, 3, 3, 3]
assert repetition(5, 0) == []
assert repetition([1, 2, 3], 5) == [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]

#Question 2
def liste_diviseurs(n: int) -> List[int]:
    """Précondition: a > 0
    Retourne la liste des diviseurs de n.
    """
    return [i for i in range(1, n+1) if n % i == 0]

#Jeu de test
assert liste_diviseurs(18) == [1, 2, 3, 6, 9, 18]
assert liste_diviseurs(5) == [1, 5]
assert liste_diviseurs(1) == [1]


def liste_diviseurs_impairs(n: int) -> List[int]:
    """Précondition: n > 0
    Retourne la liste des diviseurs de n impairs.
    """
    return [i for i in range(1, n+1)
            if n % i == 0 and i % 2 != 0]

#Jeu de test
assert liste_diviseurs_impairs(24) == [1, 3]
assert liste_diviseurs_impairs(8) == [1]
assert liste_diviseurs_impairs(15) == [1, 3, 5, 15]
