#Exercice 9.5
Produits = Dict[str, float]

#Question 1
g_s: Produits = {'Sabre Laser': 229.0,
                'Mitendo DX': 127.30,
                'Coussin Linux': 74.50,
                'Slip Goldorak': 29.90,
                'Station Nextpresso': 184.60}


#Question 2
def prix_moyen(dic: Produits) -> float:
    """Précondition: aucune
    Renvoie le prix moyens des produits de la liste dic.
    """
    prix_total: float = 0 #somme des prix des produits dans dic

    n: int = len(dic) #nombre de produits dans dic
    i: str
    for i in dic:
        prix_total = prix_total + dic[i]

    return prix_total/n

#Jeu de test
assert prix_moyen({'Sabre Laser': 229.0,
                    'Mitendo DX': 127.30,
                    'Coussin Linux': 74.50,
                    'Slip Goldorak': 29.90,
                    'Station Nextpresso': 184.60}) == 129.06


#Question 3
def fourchette_prix(mini: float, maxi: float, prix: Produits) -> \
    Set[str]:
    """Précondition: aucune
    Retourne l'ensemble de produits dont le prix est compris entre
    mini et maxi.
    """
    ens: Set[str] = set() #liste de produits

    n: str
    for n in prix:
        if prix[n] < maxi and prix[n] > mini:
            ens.add(n)
    return ens

#Jeu de test
assert fourchette_prix(50.0, 200.0, {'Sabre Laser': 229.0,
                                    'Mitendo DX': 127.30,
                                    'Coussin Linux': 74.50,
                                    'Slip Goldorak': 29.90,
                                    'Station Nextpresso': 184.60}) \
        == {'Coussin Linux', 'Mitendo DX', 'Station Nextpresso'}

assert fourchette_prix(200, 300, {'Sabre Laser': 229.0,
                'Mitendo DX': 127.30,
                'Coussin Linux': 74.50,
                'Slip Goldorak': 29.90,
                'Station Nextpresso': 184.60}) == {"Sabre Laser"}


#Question 4
Panier = Dict[str, int]
panier_g_s: Panier = {"Sabre Laser": 3,
                      "Coussin Linux": 2,
                      "Slip Goldorak": 1}


#Question 5
def tous_disponibles(panier: Panier, prix: Produits) -> bool:
    """Précondition: panier de type Panier et prix de type Produits.
    Renvoie True si tous les produits du panier sont disponibles dans
    prix.
    """
    n: str
    for n in panier:
        if n not in prix:
            return False
    return True

#Jeu de test
assert tous_disponibles({"Sabre Laser": 3,
                      "Coussin Linux": 2,
                      "Slip Goldorak": 1},
                     {'Sabre Laser': 229.0,
                      'Mitendo DX': 127.30,
                      'Coussin Linux': 74.50,
                      'Slip Goldorak': 29.90,
                      'Station Nextpresso': 184.60}) == True
assert tous_disponibles({"Stylo invisibles": 10},
                        {"Stylo bic": 20.0}) == False


#Question 6
def prix_achats(panier: Panier, prix: Produits) -> float:
    """Précondition: tous les produits du panier sont disponibles dans produits.
    Renvoie le prix total du panier.
    """
    prix_total: float = 0 #prix total du panier

    n: str
    for n in panier:
        prix_total = prix_total + panier[n] * prix[n]

    return prix_total

#Jeu de test
assert prix_achats({'Sabre Laser': 3, 'Coussin Linux': 2, 'Slip Goldorak': 1},
                    {'Sabre Laser': 229.0,
                    'Mitendo DX': 127.30,
                    'Coussin Linux': 74.50,
                    'Slip Goldorak': 29.90,
                    'Station Nextpresso': 184.60}) == 865.9
assert prix_achats({"Stylo Bic": 20}, {"Stylo Bic": 20.0}) == 400.0
