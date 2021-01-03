#Exercice 7.2
def nb_de_max(L: List[float]) -> Tuple[float, int]:
    """Précondition: len(L) > 0.
    Renvoie nombre d'occurence du nombre max de L.
    """ 
    m: float = L[0] #le nombre maximum
    n: int = 0 #nombre de fois où m est apparu

    i: float
    for i in L:
        if i > m: # on a trouvé un nouveau m
            m = i
            n = 1
        elif i == m: #on a trouvé une nouvelle occurence de m
            n = n + 1
            
    return (m, n)

#Jeu de test
assert nb_de_max([10]) == (10, 1)
assert nb_de_max([3, 7, 9, 5.4, 8.9, 9, 8.999, 5]) == (9, 2)
assert nb_de_max([-2, -1, -5, -3, -1, -4, -1]) == (-1, 3)
