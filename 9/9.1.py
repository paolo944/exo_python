#Exercice 9.1
#Question 1
def diff_sym(ens1: Set[T], ens2: Set[T]) -> Set[T]:
    """Précondition: ens1, ens2 de même type.
    Retourne la différence symétrique des deux ensembles.
    """
    ens_d: Set[T] = set()
    e1: T
    for e1 in ens1:
        if e1 not in ens2:
            ens_d.add(e1)
            
    e2: T
    for e2 in ens2:
        if e2 not in ens1:
            ens_d.add(e2)
            
    return ens_d

#Jeu de test
assert diff_sym({2, 5, 9}, {3, 5, 8}) == {2, 3, 8, 9}
assert diff_sym({2, 5, 9}, {2, 5, 8, 9}) =={8}
assert diff_sym({'a', 'b', 'c'}, {'d', 'e', 'f'}) == {'a', 'b', 'c', 'd', 'e', 'f'}
assert diff_sym({'a', 'b', 'c'}, set()) == {'a', 'b', 'c'}
assert diff_sym(set(), {'d', 'e', 'f'}) == {'d', 'e', 'f'}
assert diff_sym({'a', 'b', 'c'}, {'a', 'b', 'c'}) == set()

#Question 2
def diff_sym2(ens1: Set[T], ens2: Set[T]) -> Set[T]:
    """Précondition: ens1 et ens2 de même type.
    Retourne la différence symétrique des deux ensembles.
    """
    return ((ens1 - ens2) | (ens2 - ens1))

#Jeu de test
assert diff_sym2({2, 5, 9}, {3, 5, 8}) == {2, 3, 8, 9}
assert diff_sym2({2, 5, 9}, {2, 5, 8, 9}) =={8}
assert diff_sym2({'a', 'b', 'c'}, {'d', 'e', 'f'}) == {'a', 'b', 'c', 'd', 'e', 'f'}
assert diff_sym2({'a', 'b', 'c'}, set()) == {'a', 'b', 'c'}
assert diff_sym2(set(), {'d', 'e', 'f'}) == {'d', 'e', 'f'}
assert diff_sym2({'a', 'b', 'c'}, {'a', 'b', 'c'}) == set()
