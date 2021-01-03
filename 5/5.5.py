#Exercice 5.5:
def est_voyelle(c : str)-> bool:
    """Précondition : len(c) == 1Retourne True si et seulement si c est     une voyelleminiscule ou majuscule."""
    return(c == 'a') or (c == 'A') \
        or(c == 'e') or (c == 'E') \
        or(c == 'i') or (c == 'I') \
        or(c == 'o') or (c == 'O') \
        or(c == 'u') or (c == 'U') \
        or(c == 'y') or (c == 'Y')

# Jeu de tests
assert est_voyelle('a') == True
assert est_voyelle('E') == True
assert est_voyelle('b') == False
assert est_voyelle('y') == True
assert est_voyelle('z') == False

#Question 1:
def nb_voyelles(c: str) -> int:
    """Précondition: c est de type str
    Renvoie le nombre de voyelles dans c."""
    compte: int = 0
    l: str
    for l in c:
        if est_voyelle(l):
            compte = compte + 1
    return compte

assert nb_voyelles('la maman du petit enfant le console') == 12
assert nb_voyelles('mr brrxcx') == 0
assert nb_voyelles('ai al o ents') == 5

#Question 2:
def voyelles_accents(c: str) -> bool:
    """Précondition : len(c) == 1Retourne True si et seulement si c est     une voyelleminiscule ou majuscule."""
    return(c == 'a') or(c == 'A') \
        or(c == 'e') or(c == 'E') \
        or(c == 'i') or(c == 'I') \
        or(c == 'o') or(c == 'O') \
        or(c == 'u') or(c == 'U') \
        or(c == 'y') or(c == 'Y') \
        or(c == "À") or(c == "Â") \
        or(c == "Ä") or(c == "Ê") \
        or(c == "É") or(c == "È") \
        or(c == "Ë") or(c == "Î") \
        or(c == "Ï") or(c == "Ô") \
        or(c == "Ö") or(c == "Ù") \
        or(c == "Û") or(c == "Ü") \
        or(c == "Ÿ") or(c == "à") \
        or(c == "â") or(c == "ä") \
        or(c == "é") or(c == "è") \
        or(c == "ê") or(c == "ë") \
        or(c == "î") or(c == "ï") \
        or(c == "ô") or(c == "ö") \
        or(c == "ù") or(c == "û") \
        or(c == "ü") or(c == "ÿ")
    
def nb_voyelles_accents(c: str) -> int:
    """Précondition: c est de type str
    Renvoie le nombre de voyelles dans c."""
    compte: int = 0
    l: str
    for l in c:
        if voyelles_accents(l):
            compte = compte + 1
    return compte

assert nb_voyelles_accents('la maman du bébé le réconforte') == 11

#Question 3:
def sans_voyelle(c: str) -> str:
    """Précondition: c est de type str.
    Renvoie une chaine de caractere a partir de c mais sans les
    voyelles."""
    l: str
    c_s: str = ""
    for l in c:
        if voyelles_accents(l):
            c_s = c_s + ""
        else:
            c_s = c_s + l
    return c_s

#Jeu de test
assert sans_voyelle('aeiouy') == ""
assert sans_voyelle('la balle au bond rebondit') == 'l bll  bnd rbndt'
assert sans_voyelle('mr brrxcx') == 'mr brrxcx'

#Question 4:
def mot_mystere(c: str) -> str:
    """Précondition: c est de type str.
    Renvoie une chaine de caractere en remplacant les voyelles par des
    - """
    l: str
    c_m: str = ""
    for l in c:
        if voyelles_accents(l):
            c_m = c_m + "_"
        else:
            c_m = c_m + l
    return c_m

assert mot_mystere('aeiouy') == '______'
assert mot_mystere('la balle au bond rebondit bien') == 'l_ b_ll_ __ b_nd r_b_nd_t b__n'
assert mot_mystere('mr brrxcx') == 'mr brrxcx'
