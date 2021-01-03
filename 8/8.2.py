#Exercice 8.2
#Question 1
def alphabet() -> List[str]:
    """Retourne la liste des 26 lettres de l'alphabet.
    """
    return [chr(i) for i in range(97, 123)]

# Jeu des tests
assert alphabet() == ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#Question 2
def est_voyelle(c: str) -> bool:
    """Précondition: len(c) == 1
    Retourne True si c une voyelle sinon False.
    """
    return (c == "a") or (c == "e") or (c == "i") or \
           (c == "o") or (c == "u") or (c == "y")

#Jeu de test
assert est_voyelle("a") == True
assert est_voyelle("z") == False
assert est_voyelle("u") == True
assert est_voyelle("b") == False


#Question 3
voyelle: List[str] = [c for c in alphabet() if est_voyelle(c)]


#Question 4
consonnes: List[str] = [c for c in alphabet() if not est_voyelle(c)]
