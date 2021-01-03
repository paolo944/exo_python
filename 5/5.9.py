#Exercice 5.9:
#Question 1:
def moins_lettre(c: str, a: str) -> str:
    """Précondition: len(c) == len(a) a et c sont de type str.
    Renvoie une chaine a partir c sans la premiere occurence de a.
    Si c ne contient pas a renvoie None."""
    c_s: str = ""
    i: str
    l_s: bool = True
    for i in c:
        if i == a and l_s:
            c_s = c_s + ""
            l_s = False
        else:
            c_s = c_s + i
    if l_s:
        return "None"
    return c_s

assert moins_lettre("papa", "a") == "ppa"
assert moins_lettre("papa", "p") == "apa"
assert moins_lettre("papa", "q") == "None"

def anagramme(m1: str, m2: str) -> bool:
    """Précondition len(m1) == len(m2)
    Renvoie True si m1 est l'anagramme de m2 ou l'inverse."""
    i: int
    if len(m1) != len(m2):
        return False
    else:
         for i in range(0, len(m2)):
            if moins_lettre(m1, m2[i]) == "None":
                return False
    return True

assert anagramme("alberteinstein", "alberteinstein") == True
assert anagramme("alberteinstein", "riennestetabli") == True
assert anagramme("alberteinstein", "toutestrelatif") == False
assert anagramme("lesfeuxdelamour", "dramesexuelflou") == True
assert anagramme("parisien", "aspirine") == True
