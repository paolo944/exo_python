# Question 1
def ou(p: bool, q:bool) -> bool:
    """Retourne la disjonction de p et q."""
    if p:
        return p
    else:
        return q

def et(p: bool, q:bool) -> bool:
    """Retourne la conjonction de p et q."""
    if p:
        if q:
            return True
        else:
            return False
    else:
        return False

def non(p: bool) -> bool:
    """Retourne la négation de p."""
    if p:
        return False
    else:
        return True

assert ou(True, False) == True
assert ou(et(True, False), False) == False
assert et(ou(False, True),non(False)) == True
assert non(non(3 == 1 + 2)) == True

#Question 3

def implique(p: bool, q: bool) -> bool:
    """Retourne le résultat de 'p implique q'."""
    if ou(non(p), q):
        return True
    else:
        return False

def ou_exclusif(p: bool, q: bool) -> bool:
    """Retourne le résultat de 'p xor q'."""
    if et(p, non(q)):
        return True
    elif et(non(p), q):
        return True
    else:
        return False

assert implique(False, False) == True
assert implique(True, False) == False
assert implique(True, 3 == 3) == True
assert ou_exclusif(True, False) == True
assert ou_exclusif(3 == 2, 3 == 3) == True
assert ou_exclusif(2 == 2, 3 == 3) == False

# Question 4

def equivalent(p: bool, q: bool) -> bool:
    """Retourne True si et seulement si p et q sont équivalent."""
    if implique(p, q):
        if implique(q, p):
            return True
        else:
            return False
    return False

assert equivalent(True, 3 == 3) == True
assert equivalent(True, 3 == 4) == False
assert equivalent(3 == 2, 3 == 8) == True
