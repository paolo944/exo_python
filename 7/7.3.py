def chargement_fichier(nom_fichier : str) -> List[str]:
    """Précondition : nom_fichier est le nom d'un fichier texte
    existant
    Retourne le contenu du fichier texte identifié par nom_fichier
    sous la forme d'une liste de lignes de texte.
    """

    # Lignes contenues dans le fichier
    l1 : List[str] = []

    # Lignes sans retour charriot
    l2 : List[str] = []

    with open(nom_fichier, 'r') as f: # 'r' pour read (lecture)
        l1 = f.readlines() # opération de lecture de lignes

    # suppression des retours charriots
    ligne : str
    for ligne in l1:
        if ligne != '' and ligne[-1] == '\n':
            l2.append(ligne[:-1])
        else:
            l2.append(ligne)
    return l2


def sauvegarde_fichier(nom_fichier : str, Contenu : List[str]) -> None:
    """Précondition : nom_fichier est un nom correct de fichier
    Sauvegarde le Contenu comme lignes de texte dans le
    fichier identifié par nom_fichier
    Attention : si le fichier existe déjà son contenu sera
    effacé.
    """
    with open(nom_fichier, 'w') as f: # 'w' pour write (écriture)
        ligne : str
        for ligne in Contenu:
            f.write(ligne) # écriture de la ligne
            f.write('\n') # ajout d'un retour charriot
            
    return None

texte: str = ["Papillon voltige",
"Dans un monde",
"Sans espoir.",
"(Kobayashi Issa)"]
