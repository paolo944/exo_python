#Exercice 10.5
Carte_de_transport = Dict[str, Set[str]]
Grandes_Lignes: Carte_de_transport
Grandes_Lignes = {'Paris': {'Strasbourg', 'Dijon', 'Toulouse',
                  'Lille', 'Lyon', 'Bordeaux'},
                  'Strasbourg':{'Paris', 'Dijon', 'München'},
                  'München': {'Strasbourg'},
                  'Dijon': {'Paris', 'Strasbourg', 'Lyon', 'Toulouse'},
                  'Lyon':{'Paris', 'Dijon', 'Toulouse'},
                  'Toulouse': {'Paris', 'Lyon', 'Dijon', 'Bordeaux'},
                  'Bordeaux': {'Nantes', 'Paris'},
                  'Nantes': {'Paris', 'Bordeaux','Quimper'},
                  'Quimper':{'Nantes'}, 'Ajaccio': {'Bastia'},
                  'Bastia': {'Ajaccio'}, 'Lille': {'Paris'}}



#Question 1:
def trajet_direct(carte: Carte_de_transport, st1: str, st2: str) -> bool:
    """Précondition: carte de type Grande_Ligne et st1 et st2 de type
    str. st1 est une clé dans carte
    Retourne True s'il existe un trajet directe entre st1 et st2.
    """
    i: str
    for i in carte[st1]:
        if i == st2:
            return True
    return False

#Jeu de test
assert trajet_direct(Grandes_Lignes, 'Paris', 'Bordeaux') == True
assert trajet_direct(Grandes_Lignes, 'Paris', 'Ajaccio') == False


#Question 2:
def ajout_station(station: str, correspondances: Set[str], carte: Carte_de_transport) -> Carte_de_transport:
    """Préconditio: les stations de correspondances existent deja dans
    carte.
    Retourne la nouvelle carte contenant les nouvelles correspondances.
    """
    carte2: Carte_de_transport = carte
    carte2[station] = correspondances
    st: str
    for st in correspondances:
        carte2[st].add(station)
    return carte2

#Jeu de test
Nouvelles_Lignes : Dict[str, Set[str]]
Nouvelles_Lignes = ajout_station('Limoges', {'Paris', 'Toulouse', 'Bordeaux'}, Grandes_Lignes)
assert trajet_direct(Nouvelles_Lignes, 'Limoges', 'Paris') == True
assert trajet_direct(Nouvelles_Lignes, 'Bordeaux', 'Limoges') == True
assert trajet_direct(Nouvelles_Lignes, 'Limoges', 'Dijon') == False


#Question 3:
def stations_atteignables(carte: Carte_de_transport, station: str, nb: int) -> Set[str]:
    """Précondition: station existe dans carte.
    Retourne le nombre de station atteignables dans un certain nb de correspondance.
    """
    cor: Set[str] = {station}
    i: int
    for i in range(nb):
        st: str
        cor2: Set[str] = set()
        for st in cor:
            cor2 = cor2 | carte[st]
        cor = cor2
    return cor

#Jeu de test
assert stations_atteignables(Grandes_Lignes, 'Paris', 0) == {"Paris"}
assert stations_atteignables(Grandes_Lignes, 'Paris', 1) == {'Bordeaux', 'Dijon', 'Lille', 'Lyon', 'Strasbourg', 'Toulouse'}
assert stations_atteignables(Grandes_Lignes, 'Paris', 2) == {'Bordeaux', 'Dijon', 'Lyon', 'München', 'Nantes', 'Paris', 'Strasbourg', 'Toulouse'}
