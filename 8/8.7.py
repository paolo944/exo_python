#Exercice 8.7
#Question 1
def triplets(n: int) -> List[Tuple[int, int, int]]:
    """Précondition: aucune
    Retourne la liste des triplets de 1 à n.
    """
    return [(i, j, k) for i in range(1, n+1)
            for j in range(1, n+1)
            for k in range(1, n+1)]

#Jeu de test
assert triplets(0) == []
assert triplets(1) == [(1, 1, 1)]
assert triplets(2) == [(1, 1, 1),
(1, 1, 2),
(1, 2, 1),
(1, 2, 2),
(2, 1, 1),
(2, 1, 2),
(2, 2, 1),
(2, 2, 2)]

#Question 2
def decompo(n: int) -> List[Tuple[int, int, int]]:
    """Précondition: aucune
    Retourne les décompositions sur un intervalle c'est à dire i+j = k.
    """
    
