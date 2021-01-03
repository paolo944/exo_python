#Exercice 6.9
#Question 1
def jonction(l : List[str], c : str) -> str:
    """Précondition : len(c) = 1
    Retourne la chaîne composée de la jonction des
    chaîne de L séparées deux-à-deux par le
    caractère séparateur c."""
    lr: str = ""
    print(lr)
    i: int
    if len(l) == 0:
        return lr
    else:
        lr = l[0]
        for i in range(1, len(l)):
            lr = lr + c + l[i]
        return lr

#Jeu de test
assert jonction(['un', 'deux', 'trois', 'quatre'], '.') == "un.deux.trois.quatre"
assert jonction(['les', 'mots', 'de', 'cette', 'phrase'], ' ') == "les mots de cette phrase"
assert jonction(['un'], '+') == "un"
assert jonction([], '+') == ""

#Question 2
def separation(s : str, c :str) -> List[str]:
    """Précondition : len(c) = 1
    retourne la liste de chaînes composées des sous-chaînes
    de s séparées par le caractère séparateur c.
    Le séparateur c n'est pas présent dans la chaîne résultat."""
    lr: List[str] = []
    if len(s) == 0:
        return lr
    else:
        p: str = ""
        i: str
        for i in s:
            if i == c:
                lr.append(p)
                p = ""
            else:
                p = p + i
        lr.append(p)
        return lr
            
#Jeu de test
assert separation('un.deux.trois.quatre', '.') == ['un', 'deux', 'trois', 'quatre']
assert separation('les mots de cette phrase', ' ') == ['les', 'mots', 'de', 'cette', 'phrase']
assert separation('les mots de cette phrase', '.') == ['les mots de cette phrase']
assert separation('', '+') == []
