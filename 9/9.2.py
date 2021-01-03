#Exercice 9.2
#Question 1
def repetes(l: List[T]) -> Set[T]:
    """Retourne l'ensemble des éléments répétés au moins une fois
    dans la liste.
    """
    ens: Set[T] = set()
    vus : Set[T] = set() 
    e : T
    for e in l:
        if e in vus: # déjà vu ?
            ens.add(e) # répétition
        else:
            vus.add(e) # c'est tout vu !
    return ens


#Jeu de test
assert repetes([1, 2, 23, 9, 2, 23, 6, 2, 9]) == {2, 9, 23}
assert repetes([1, 2, 3, 4]) == set()
assert repetes(['bonjour', 'ça', 'ça', 'va', '?']) == {"ça"}

#Question 2
def sans_repetes(l: List[T]) -> List[T]:
    """Retourne l'esnemble des éléments de l sans réptitions.
    """
    vus: Set[T] = set()

    lr: List[T] = []


    e: T
    for e in l:
        if e not in vus:
            lr.append(e)
            vus.add(e)
    return lr

#Jeu de test
assert sans_repetes([1, 2, 23, 9, 2, 23, 6, 2, 9]) == [1, 2, 23, 9, 6]
assert sans_repetes([1, 2, 3, 4]) == [1, 2, 3, 4]
assert sans_repetes([2, 1, 2, 1, 2, 1, 2]) == [2, 1]
assert sans_repetes(['bonjour', 'ça', 'ça', 'va' , '?']) == ['bonjour', 'ça', 'va', '?']


#Question 3
def uniques(l: List[T]) -> Set[T]:
    """Précondition: aucune
    Retourne l'ensemble des éléments de l apparaissant qu'une seule
    fois.
    """
    unefois : Set[T] = set()
    trop : Set[T] = set()
    e : T
    for e in l:
        if e in unefois:
    # vu au moins 2 fois
            trop.add(e)
        else:
            # vu pour la première fois
            unefois.add(e)
    return unefois - trop

#Jeu de test
assert uniques([1, 2, 23, 9, 2, 23, 6, 2, 1]) == {6, 9}
assert uniques([1, 2, 1, 1]) == {2}
assert uniques([1, 2, 1, 2, 1]) == set()
