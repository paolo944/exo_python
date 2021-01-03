#Exercice 7.6

Etudiant = Tuple[str, str, int, List[int]]

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

#Question 2
BaseUPMC : List[Etudiant]
BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]

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

#Jeu de test
assert moyenne_generale(BaseUPMC) == 11.307142857142857
assert moyenne_generale([]) == 0.0

#Question 3
def top_etudiant(bd : List[Etudiant]) -> Tuple[str, str]:
    """Précondition : len(bd) > 0
    retourne un étudiant de la base bd avec la meilleure
    moyenne. Si des étudiants sont ex-aequo alors on
    retourne le premier dans l'ordre séquentiel de la liste.
    """
    nom_top: str
    prenom_top: str
    maximum: float = 0
    etudiant: Etudiant
    for etudiant in bd:
        nom, prenom, _, notes = etudiant
        if note_moyenne(notes) > maximum:
            maximum = note_moyenne(notes)
            nom_top = nom
            prenom_top = prenom
    return (nom_top, prenom_top)

#Jeu de test
assert top_etudiant(BaseUPMC) == ('ALEZE', 'Blaise')

#Question 4
def recherche_moyenne(num: int, base: List[Etudiant]) -> Optional[float] :
    """Précondition:
    Retourne la moyenne de l'étudiant grâce au numéro donné sauf si ce
    numéro n'existe pas dans la base de données donnée.
    """
    etudiant: Etudiant
    for etudiant in base:
        _, _, num_e, notes = etudiant
        if num_e == num:
            return note_moyenne(notes)
    return None

assert recherche_moyenne(20244229, BaseUPMC) == 11.8
assert recherche_moyenne(20342241, BaseUPMC) == 10.5
assert recherche_moyenne(2024129111, BaseUPMC) == None
