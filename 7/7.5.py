#Exercice 7.5

Point = Tuple[int, int]

#Question 1
def vecteur(p1: Point, p2: Point) -> Point:
    """Précondition
    Renvoie le vecteur composé des points p1 et p2.
    """
    a, b = p1
    c, d = p2
    return (c - a, d - b)
    
#Jeu de test
assert vecteur((3, 2), (5, 4)) == (2, 2)
assert vecteur((20, 5), (21, 6)) == (1, 1)

#Question 2
def alignes(p1: Point, p2: Point, p3: Point) -> bool:
    """Précondition:
    Retourne True si les points sont alignés sinon retourne False.
    """
    v1 = vecteur(p1, p2)
    v2 = vecteur(p2, p3)
    
