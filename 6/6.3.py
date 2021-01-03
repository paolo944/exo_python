#Exercice 6.3
#Question 1
def liste_div(a: int) -> List[int]:
    """Précondition: a > 0.
    Retourne la liste de diviseurs de a."""
    lr: List[int] = []
    i: int
    for i in range(1, a+1):
        if a % i == 0:
            lr.append(i)
    return lr

#Jeu de test
assert liste_div(18) == [1, 2, 3, 6, 9, 18]
assert liste_div(12) == [1, 2, 3, 4, 6, 12]
assert liste_div(25) == [1, 5, 25]

#Question 2
def liste_div_impairs(a: int) -> List[int]:
    """Précondition: a > 0.
    Retourne la liste de diviseurs impairs de a."""
    lr: List[int] = []
    i: int = 1
    while i < a + 1:
        if a % i == 0:
            lr.append(i)
        i = i + 2
    return lr

assert liste_div_impairs(24) == [1, 3]
assert liste_div_impairs(1) == [1]
assert liste_div_impairs(15) == [1, 3, 5, 15]
