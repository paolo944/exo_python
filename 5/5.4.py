#Exercice 5.4:
#Question 1:
def suppression_debut(l: str, c: str) -> str:
    """Précondition: len(l) == 1 et type de l et c str.
    Renvoie c sans la premiere occurence de l."""
    c_s: str = ""
    a: str
    l_s: bool = True
    for a in c:
        if a == l and l_s:
            c_s = c_s + ""
            l_s = False
        else:
            c_s = c_s + a
    return c_s
        
assert suppression_debut("a", "") == ""
assert suppression_debut("a", "aaaaa") == "aaaa"
assert suppression_debut("p", "le papa noel") == "le apa noel"
assert suppression_debut("a", "bbbbb") == "bbbbb"

#Question 2:
def suppression_derniere(l: str, c: str) -> str:
    """Précondition: len(l) == 1 et type de l et c str.
    Renvoie c sans la derniere occurence de l."""
    c_s : str = ""
    i: int = len(c) -1
    l_s: bool = True
    while i >= 0:
        if c[i] == l and l_s:
            c_s == c_s + ""
            l_s = False
        else:
            c_s = c[i] + c_s
        i = i - 1
    print(c_s)
    return c_s

assert suppression_derniere("a","") == ""
assert suppression_derniere("a","aaaaa") == "aaaa" 
assert suppression_derniere("p","le papa noel") == "le paa noel"
assert suppression_derniere("a","bbbbb") == "bbbbb"
