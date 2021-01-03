#Exercice 7.4
#Question 1
Fraction = Tuple[int, int]

def pgcd(c: Fraction) -> int:
    """Précondition:
    Retourne le pgcd du numérateur et du déniminateur.
    """
    n: int = 1
    a, b = c
    if a < b:
        while n != 0:
            n = b % a
            b = a
            a = n
        return n + b
    else:
        while n != 0:
            n = a % b
            a = b
            b = n
        return n + a

#Jeu de test
assert pgcd((561, 357)) == 51
assert pgcd((42, 63)) == 21
assert pgcd((36, 60)) == 12

def fraction(a: int, b: int) -> Fraction:
    """Précondition: b != 0 et a et b sont de type int.
    Retourne la fraction canonique.
    """
    p: int = pgcd((a, b))
    return (a//p, b//p)

#Jeu de test
assert fraction(9, 12) == (3, 4)
assert fraction(12, 9) == (4, 3)
assert fraction(180, 240) == (3, 4)

assert fraction(121, 187) == (11, 17)

#Question 2
def frac_mult(c: Fraction, d: Fraction) -> Fraction:
    """Précondition: b non nul.
    Retourne la multiplication de deux fraction sous forme canonique.
    """
    a, b = c
    e, f = d
    t: int = a * e
    i: int = b * f
    p: int = pgcd((t, i))
    return ((t // p, i // p))

#Jeu de test
assert frac_mult( (3, 4), (8, 4) ) == (3, 2)
assert frac_mult( (3, 4), (4, 3) ) == (1, 1)
assert frac_mult( (3, 4), (1, 1) ) == (3, 4)

#Quesrion 3
def frac_div(c: Fraction, d: Fraction) -> Fraction:
    """Précondition: b non nul.
    Retourne la division de deux fraction sous forme canonique.
    """
    a, b = c
    e, f = d
    return frac_mult((a,b), (f, e))

#Jeu de test
assert frac_div( (3, 4), (8, 4) ) == (3, 8)
assert frac_div( (3, 4), (4, 3) ) == (9, 16)
assert frac_div( (3, 4), (1, 1) ) == (3, 4)

#Question 4
def ppcm(a : int, b : int) -> int:
    """Précondition : (a != 0) and (b != 0)
    Retourne le plus petit commun multiple de a et b.
    """
    # pgcd de a et b
    p : int = 0
    if a >= b:
        p = pgcd((a, b))
    else:
        p = pgcd((b, a))
    return (a * b) // p

#Jeu de test
assert ppcm(3, 4) == 12
assert ppcm(4, 3) == 12
assert ppcm(11, 17) == 187
assert ppcm(15, 9) == 45

def frac_add(e: Fraction, f: Fraction) -> Fraction:
    """Précondition: pas de numérateur = 0.
    Retourne l'addition des fractions c et d.
    """
    a, b = e
    c, d = f
    p: int = ppcm(b, d)
    r: int = (a*(p//b)+c*(p//d))
    g: int = pgcd((r, p))
    return ((r//g, p//g))

#Jeu de test
assert frac_add( (8, 4), (1, 4) ) == (9, 4)
assert frac_add( (9, 4), (5, 4) ) == (7, 2)
assert frac_add( (1, 3), (1, 2) ) == (5, 6)
