def fermat(n: float) -> float:
    # cette fonction retourne le n-ième nombre de fermat
    # Pas de précondition
    return 2**2**n + 1

assert fermat(0) == 3
assert fermat(1) == 5
assert fermat(2) == 17
assert fermat(5) == 4294967297

""" Ici nous prouvons que f(5) n'est pas un nombre premier en trouvent
le reste de sa division par 641 """
assert fermat(5) % 641 == 0

""" f(5) n'est pas prémier car nous trouvons comme résultat de la
divison 0 """
