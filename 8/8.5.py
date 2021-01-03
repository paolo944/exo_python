#Exercice 8.5
#Question 1
def liste_caracteres(c: str) -> List[str]:
    """Précondition: type(c) == str
    Retourne la liste des caracteres de c.
    """
    return [i for i in c]

#Jeu de test
assert liste_caracteres('les carottes') == ['l', 'e', 's', ' ', 'c', 'a', 'r', 'o', 't', 't', 'e', 's']
assert liste_caracteres('') == []

#Question 2
def chaine_de(l: List[str]) -> str:
    """Précondition: type(l) == List[str]
    Retourne la chaine de caractere correspondant à la liste de
    caractère dans l.
    """
    c: str = ""
    i: str
    for i in l:
        c = c + i
    return c

#Jeu de test
assert chaine_de(['s','a','l','u','t']) == "salut"
assert chaine_de([]) == ""
assert chaine_de(liste_caracteres('les carottes')) == "les carottes"

#Question 3
def num_car(c: str) -> int:
    """Précondition: len(c) == 1.
    Retourne le numéro d'ordre du caractère c dans l'alphabet.
    """
    return ord(c) - 97

#Jeu de test
assert num_car('a') == 0
assert num_car('b') == 1
assert num_car('z') == 25

#Question 4
def car_num(n: int) -> str:
    """Précondition: n compris entre 0 et 25.
    Retourne le caractère correspondant à n.
    """
    return chr(n + 97)

#Jeu de test
assert car_num(0) == "a"
assert car_num(1) == "b"
assert car_num(25) == "z"

#Question 5
def rot13(c: str) -> str:
    """Précondition: len(c) == 1
    Retourne un le code de c selon ROT13.
    """
    nomb: List[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
    n: int = num_car(c)
    if n < 0 or n > 25:
        return c
    else:
        if n >= 13:
            return car_num((n+13) % 26)
        return car_num(n+13)

#Jeu de test
assert rot13('a') == "n"
assert rot13('b') == "o"
assert rot13('l') == "y"
assert rot13('m') == "z"
assert rot13('n') == "a"
assert rot13('o') == "b"
assert rot13('z') == "m"
assert rot13(rot13('z')) == "z"
assert rot13('8') == "8"
assert rot13(' ') == " "

#Question 6
def codage_rot13(c: str) -> str:
    """Précondition: type(c) == str
    Retourne le codage de c selon ROT13.
    """
    l_rot13: List[str] =  [rot13(i) for i in c]
    return chaine_de(l_rot13)

#Jeu de test
assert codage_rot13('abcdef') == 'nopqrs'
assert codage_rot13('nopqrs') =='abcdef'
assert codage_rot13('les carottes sont cuites') == 'yrf pnebggrf fbag phvgrf'
assert codage_rot13('yrf pnebggrf fbag phvgrf') == 'les carottes sont cuites'
assert codage_rot13('nowhere gnat chechen') =='abjurer tang purpura'
