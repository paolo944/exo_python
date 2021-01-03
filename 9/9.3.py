#Exercice 9.3
Recette = Dict[str, Set[str]]
Dessert : Recette
Dessert = {
'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'}
,'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'}
,'crepes' : {'oeuf', 'farine', 'lait'}
,'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'}
,'kouign amann' : {'farine', 'beurre', 'sucre'}
}


#Question 1
def nb_ingredients(des: Recette, r: str) -> int:
    """Précondition:
    Retourne le nombre d'ingrédients contenu dans la recette
    """
    return len(des[r])

#Jeu de test
assert nb_ingredients(Dessert, 'crepes') == 3
assert nb_ingredients(Dessert, 'gateau chocolat') == 5

#Question 2:
def recette_avec(des: Recette, ing: str) -> Set[str]:
    """Précondition:
    Retourne l'ensemble des recettes contenant l'ingrédient ing.
    """
    ens: Set[str] = set()
    i: str
    for i in des:
        if ing in des[i]:
            ens.add(i)
    return ens

#Jeu de test
assert recette_avec(Dessert, 'beurre') == {'gateau chocolat', 'kouign amann', 'quatre-quarts'}
assert recette_avec(Dessert, 'lait') == {'crepes'}
assert recette_avec(Dessert, 'fraise') == set()

#Question 3
def tous_ingredients(des: Recette) -> Set[str]:
    """Précondition:
    Retourne l'ensemble des ingrédients de toutes les recettes.
    """
    ens: Set[str] = set()
    e: str
    for e in des:
        ens = ens | des[e]
    return ens

#Jeu de test
assert tous_ingredients(Dessert) == {'beurre', 'chocolat', 'farine', 'lait', 'oeuf', 'sucre', 'yaourt'}

#Question 4
def table_ingredients(des: Recette) -> Recette:
    """Précondition:
    Retourne la table des ingrédients avec un ensemble de leur dessert
    """
    table: Dict[str, Set[str]] = dict()
    ingredients: Set[str] = tous_ingredients(des)
    i: str
    for i in ingredients:
        table[i] = recette_avec(des, i)
    return table

#Jeu de test
assert table_ingredients(Dessert) \
    == {'lait': {'crepes'}
    ,'beurre': {'gateau chocolat', 'quatre-quarts', 'kouign amann'}
    ,'oeuf': {'gateau chocolat', 'quatre-quarts',
    'crepes', 'gateau yaourt'}
    ,'yaourt': {'gateau yaourt'}
    ,'sucre': {'kouign amann', 'gateau chocolat'
    ,'quatre-quarts', 'gateau yaourt'}
    ,'farine': {'kouign amann', 'gateau chocolat'
    ,'quatre-quarts', 'crepes', 'gateau yaourt'}
    ,'chocolat': {'gateau chocolat'}}
assert table_ingredients(dict()) == dict()

#Question 5
def ingredient_principal(des: Recette) -> str:
    """Précondition:
    Retourne l'ingrédient le plus utilisé.
    """
    table: Dict[str, Set[str]] = table_ingredients(des)
    ires: str = ""
    n: int = 0
    i: str
    for i in table:
        if len(table[i]) > n:
            ires = i
            n = len(table[i])
    return ires

# Jeu de tests
assert ingredient_principal(Dessert) == 'farine'
assert ingredient_principal({'A' : {'a', 'b'},
'B' : {'a', 'c'}}) == 'a'
assert ingredient_principal({'A' : {'a', 'b'},
'B' : {'a', 'b'}}) in {'a', 'b'}

#Question 6
def recettes_sans(des: Recette, i: str) -> Recette:
    """Précondition:
    Retourne un nouveau livre de recette sans les recettes contenant
    l'ingrédient i.
    """
    des_sans: Recette = dict()
    n : str
    for n in des:
        if i not in des[n]:
            des_sans[n] = des[n]
    return des_sans

#Jeu de test
assert recettes_sans(Dessert, 'farine') == dict()
assert recettes_sans(Dessert, 'oeuf') == {'kouign amann': {'beurre', 'farine', 'sucre'}}
assert recettes_sans(Dessert, 'beurre') == {'gateau yaourt': {'farine', 'oeuf', 'sucre', 'yaourt'},
'crepes': {'farine', 'lait', 'oeuf'}}
