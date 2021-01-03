#Exercice 5.8:
def est_chiffre(c : str) -> bool:
    """Précondition : len(c) == 1Retourne True si et seulement si c est     un chiffre.55
    """
    return('0' <= c) and (c <= '9')

# Jeu de tests
assert est_chiffre('4') == True
assert est_chiffre('9') == True
assert est_chiffre('x') == False

#Question 1:
#def decompression(c: str) -> str:
"""Précondition: c est de type str.
Renvoie la chaine de caractère decompressé s'il le faut"""
"""    c_d: str = ""
    i: int = 0
    while i < len(c):
        if est_chiffre(c[i]):
            n: int = int(c[i])
            c_d = c_d + n * c[i+1]
            i = i + 2
        else:
            c_d = c_d + c[i]
            i = i + 1
    return c_d
            
assert decompression('ab3cd') == 'abcccd'
assert decompression('ab3c2d4efgh') == 'abcccddeeeefgh'
assert decompression('abcdefg') == 'abcdefg'
"""
#Question 2:
def compression(c: str) -> str:
    """Précondition: c de type str et sans entier.
    Renvoie la chaine de caractère c compressé selon le principe RLE"""
    c_c: str = ""
    i: int = 0
    j: int = 0
    while i < len(c):
        count: int= 1
        j = i
        if c[j] == c[j+1]:
            while j < len(c) and c[j] == c[j+1]:
                count = count + 1
                j = j + 1
            c_c = c_c + str(count) + c[i]
            i = i + count - 1
        else:
            c_c = c_c + c[i]
            i = i + 1
    return c_c
            
assert compression('abcccddeeeefgh') == 'ab3c2d4efgh'
    
    
