#Exercice 5.3:
#Question 1:
def est_palindrome(c: str) -> bool:
    """Précondition: c est un str.
    Renvoie True si c est palindrome sinon revoie False."""
    i : int
    for i in range(0, len(c)//2):
        if c[i]!= c[-i-1]:
            return False
    return True

assert est_palindrome("") == True
assert est_palindrome("je ne suis pas palindrome") == False
assert est_palindrome("aba") == True
assert est_palindrome("amanaplanacanalpanama") == True

#Question 2:
def miroir(c: str) -> str:
    """Précondition: c de type str.
    Renvoie un palindrome de c."""
    c_m: str = ""
    a: str
    for a in c:
         c_m = a + c_m
    return c + c_m

assert miroir("abc") == "abccba"
assert miroir("amanaplanacanal") == "amanaplanacanallanacanalpanama"
assert miroir("do-re-mi-fa-sol") == "do-re-mi-fa-sollos-af-im-er-od"
