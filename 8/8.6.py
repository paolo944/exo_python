#Exercice 8.6
Etudiant = Tuple[str, str, int, List[int]]
BaseUPMC : List[Etudiant]
BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]

#Question 1
#Question 1
def note_moyenne(notes: List[float]) -> float:
    """Précondition:
    Retourne le moyenne des notes de l'étudiant.
    """
    if len(notes) == 0:
        return 0.0
    else:
        i: float
        s: float = 0
        for i in notes:
            s = s + i
        return s/len(notes)

assert note_moyenne([12, 8, 14, 6, 5, 15])  == 10.0
assert note_moyenne([]) == 0.0

def moyenne_generale(base: List[Etudiant]) -> float:
    """Précondition:
    Retourne la moyenne générale de la base d'étudiant.
    """
    if len(base) == 0:
        return 0.0
    else:
        s: float = 0
        etudiant: Etudiant
        for etudiant in base:
            _, _, _, notes = etudiant
            s = s + note_moyenne(notes)
        return s/len(base)


def mauvaise_note(etu: Etudiant) -> bool:
    """Précondition:
    Retourne True si etu a au moins une note inférieur à la moyenne.
    """
    moyenne: float = moyenne_generale(BaseUPMC)
    _, _, _, notes = etu
    note: float
    for note in notes:
        if note < moyenne:
            return True
    return False

#Jeu de test
assert mauvaise_note(('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9])) == True
assert mauvaise_note(('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20])) == False
assert mauvaise_note(('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5])) == True
