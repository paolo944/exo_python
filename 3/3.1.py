def somme_impairs_inf(n : int) -> int:
    """Précondition: n >= 0
    Retourne la somme des entiers impairs à partir de 1
    jusqu'à n.
    """
    somme : int = 0
    i: int = 1
    while i <= n:
        somme = somme + i
        i = i + 2
    return somme

# Jeu de test
assert somme_impairs_inf(1) == 1
assert somme_impairs_inf(2) == 1
assert somme_impairs_inf(5) == 9
assert somme_impairs_inf(8) == 16
