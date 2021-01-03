#Exercice 5.6:
#QuestAion 1:
def base_comp(c: str) -> str:
    """Précondition: len(c) == 1 et c de type str
    Renvoie la base complémentaire à c."""
    if c == "C":
        return "G"
    elif c == "G":
        return "C"
    elif c == "T":
        return "A"
    elif c == "A":
        return "T"
    elif c == "":
        return ""
    else:
        return "Erreur"

#Jeu de test:
assert base_comp("C") == "G"
assert base_comp("G") == "C"
assert base_comp("T") == "A"
assert base_comp("A") == "T"
assert base_comp("") == ""

#Question 2:
def brin_comp(c: str) -> str:
    """Précondition: c de type str.
    Renvoie le brin complémentaire de c."""
    brin_c: str = ""
    i: str
    for i in c:
        brin_c = base_comp(i) + brin_c
    return brin_c

#Jeu de test
assert brin_comp('ATCG') == 'CGAT'
assert brin_comp('ATTGCCGTATGTATTGCGCT') == 'AGCGCAATACATACGGCAAT'
assert brin_comp("") == ""

#Question 3:
def test_comp(c: str, b: str) -> bool:
    """Précondition: c et b de type str.
    Renvoie True si b est le brin complémentaire de c."""
    i: str
    n: int = len(c) - 1
    if len(c) == len(b):
        for i in b:
            if base_comp(i) == c[n]:
                n = n - 1
            else:
                return False
        return True
    else:
        return False

#Jeu de test
assert test_comp('','') == True
assert test_comp('','ATCG') == False
assert test_comp('ATCG','') == False
assert test_comp('ATCG','CGAT') == True
assert test_comp('ATCG','TAAG') == False
assert test_comp('ATTGCCGTATGTATTGCGCT','AGCGCAATACATACGGCAAT') == True

#Question 4:
def sous_seq(c: str, b: str) -> bool:
    """Précondition: c et b de type str.
    Renvoie True si c est une sous-sequence de b."""
    i: int
    if c == "":
        return True
    else:
        for i in range(len(b) - len(c) + 1):
            if c == b[i: i + len(c)]:
                return True
        return False

#Jeu de test
assert sous_seq('','') == True
assert sous_seq('','ATCG') == True
assert sous_seq('ATCG','') == False
assert sous_seq('GC','TAGC') == True
assert sous_seq('GC','TAAG') == False
assert sous_seq('CA','TAACGGCATACATAACGCGA') == True

#Question 5:
def recherche_sous_seq(c: str, b: str) -> int:
    """Précondition: c et b de type str.
    Renvoie le numero de l'indice correspondant au début de c si c es t une sous-séquence de b."""
    i: int
    if c == "":
        return 0
    else:
        for i in range(len(b) - len(c) + 1):
            if c == b[i: i + len(c)]:
                return i
        return None

assert recherche_sous_seq('','') == 0
assert recherche_sous_seq('','ATCG') == 0
assert recherche_sous_seq('ATCG','') == None
assert recherche_sous_seq('GC','TAGC') == 2
assert recherche_sous_seq('GC','TAAC') == None
assert recherche_sous_seq('CATA','TAACGGCATACATAACGCGA') == 6
