#Exercice 8.3
#Question 1
def liste_non_multiple(n: int, l: List[int]) -> List[int]:
    """Précondition: n != 0
    Retourne la liste de entiers non multiples de n et contenu dans l.
    """
    return [i for i in l if i % n != 0]

#Jeu de test
assert liste_non_multiple(2,[2,3,4,5,6,7,8,9,10]) == [3, 5, 7, 9]
assert liste_non_multiple(3,[2,3,4,5]) == [2, 4, 5]
assert liste_non_multiple(2,[2,4,6]) == []
assert liste_non_multiple(2,[]) == []
assert liste_non_multiple(7,[2,3,4,5]) == [2, 3, 4, 5]


#Question 2
def eratosthene(n: int) -> List[int]:
    """Précondition: n > 0
    Retourne la liste des entiers de 2 à n.
    """
    l: List[int] = [k for k in range(2, n+1)]
    lp: List[int] = []
    p: int = 0
    while len(l) > 0:
        p = l[0]
        lp.append(p)
        l = liste_non_multiple(p, l)
    return lp

#Jeu de test
assert eratosthene(10) == [2,3,5,7]
assert eratosthene(2) == [2]
assert eratosthene(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]



#Question 3
def liste_facteurs_premiers(n: int) -> List[int]:
    """Précondition: > 1
    Retourne la liste des facteurs premiers de n.
    """
    return [i for i in eratosthene(n) if n%i == 0]

#Jeu de test
assert liste_facteurs_premiers(2) == [2]
assert liste_facteurs_premiers(10) == [2, 5]
assert liste_facteurs_premiers(2*3*7) == [2, 3, 7]
assert liste_facteurs_premiers(2*3*4*7*9) == [2, 3, 7]
