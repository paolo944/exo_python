#Exercice 6.1
#Question 1
def reptition(x: T, k: int) -> List[T]:
    """Précondition :k >= 0
    Retourne la liste avec x occurence de k"""
    lr: List[T] = []
    i: int
    for i in range(k):
        lr.append(x)
    return lr

#Jeu de test
assert reptition(0, 4) == [0, 0, 0, 0]
assert reptition(4, 0) == []
assert reptition("pom", 5) == ["pom", "pom", "pom", "pom", "pom"]

#Question 2
def repetition_bloc(l: List[T], k: int) -> List[T]:
    """Retourne une liste concatenant k fois la liste l"""
    lr: List[T] = l * k
    return lr

assert repetition_bloc(["chat", "thon", "loup"], 3) == ['chat', 'thon', 'loup', 'chat', 'thon', 'loup', 'chat', 'thon', 'loup']
assert repetition_bloc([1, 2, 3], 5) == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

assert repetition_bloc([1, 2, 3, 4, 5], 0) == []
