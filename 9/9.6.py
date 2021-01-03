#Exercice 9.6
Dictionnaire = Dict[str, str]

Dict_Ang_Fra : Dictionnaire
Dict_Ang_Fra = {'the': 'le', 'cat': 'chat',
'fish': 'poisson', 'catches': 'attrape'}

Dict_Fra_Ita : Dictionnaire
Dict_Fra_Ita = {'le': 'il', 'chat': 'gatto',
'poisson': 'pesce', 'attrape': 'cattura'}

#Question 1
def traduction_mot_a_mot(l: List[str], dico: Dictionnaire) -> \
List[str]:
    """Précondition: l est la clé dans le dictionnaire.
    retourne la traduction de la liste de mot l dans le dictionnaire
    dico donné.
    """
    l_r: List[str] = [] #liste de mot traduis
    
    i: str
    for i in l:
        l_r.append(dico[i])
    return l_r

#Jeu de test
assert traduction_mot_a_mot([],Dict_Ang_Fra) == []
assert traduction_mot_a_mot(['cat'],Dict_Ang_Fra) == ["chat"]
assert traduction_mot_a_mot(['the', 'cat', 'catches', 'the', 'fish'],
Dict_Ang_Fra) == ['le', 'chat', 'attrape', 'le', 'poisson']
assert traduction_mot_a_mot(['le', 'chat', 'attrape', 'le', 'poisson'],
Dict_Fra_Ita) == ['il', 'gatto', 'cattura', 'il', 'pesce']


#Question 2
def dictionnaire_inverse(dico: Dictionnaire) -> Dictionnaire:
    """Précondition: un élément ne doit apparaître qu'une seule fois
    dans le dictionnaire.
    Retourne le dictionnaire inverse de dico.
    """
    dico_inv: Dictionnaire = dict() #dictionnaire inversé

    i: str
    for i in dico:
        dico_inv[dico[i]] = i

    return dico_inv
    
#Jeu de test
assert dictionnaire_inverse({"cat": "chat"}) == {"chat": "cat"}
assert dictionnaire_inverse(Dict_Ang_Fra) == \
{'poisson': 'fish', 'le': 'the', 'chat': 'cat', 'attrape': 'catches'}
assert dictionnaire_inverse(Dict_Fra_Ita) == \
{'pesce': 'poisson', 'il': 'le', 'gatto': 'chat', 'cattura': 'attrape'}


#Question 3
def composition_dictionnaires(dico1: Dictionnaire, dico2: Dictionnaire) \
-> Dictionnaire:
    """Précondition: aucune
    Renvoie le dictionnaire correspondant à la composition de dico1 et
    dico2.
    """
    dico3: Dictionnaire = dict() #dictionnaire final

    i: str
    for i in dico1:
        dico3[i] = dico2[dico1[i]]

    return dico3

#Jeu de test
assert composition_dictionnaires({"chat":"cat"}, {"cat":"gatto"}) == \
       {"chat": "gatto"}
assert composition_dictionnaires(Dict_Ang_Fra, Dict_Fra_Ita) == \
       {'fish': 'pesce', 'catches': 'cattura', 'the': 'il', 'cat': 'gatto'}
