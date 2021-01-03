def factorielle(n: int) -> int:
    i: int
    s: int = 1
    for i in range(2, n+1):
        s = s * i
        print("s est égale à", s, "au bout de", i-1, "tour(s)")
    return s

assert factorielle(3) == 6
assert factorielle(2) == 2

def repit(c: str, n: int) -> str:
    i: int
    c_final: str = ""
    for i in range(1, n+1):
        c_final = c_final + c
    return c_final

def occurences(l: str, c: str) -> int:
    compte: int = 0
    mon_cul : str
    for mon_cul in c:
        if mon_cul == l:
            compte = compte + 1
    return compte

def presence(l: str, c: str) -> bool:
    lettre : str
    for lettre in c:
        if lettre == l:
            return True
    return False

def rech(l: str, c: str) -> int:
    i: int
    for i in range(len(c)):
        if c[i] == l:
            return i
    else:
        return None

def sub(l: str, l2: str, c: str) -> str:
    c_sub: str = ""
    lettre: str
    for lettre in c:
        if lettre == l:
            c_sub = c_sub + l2
        else:
            c_sub = c_sub + lettre
    return c_sub

def suppr(l: str, c: str) -> str:
    c_suppr: str = ""
    lettre: str
    for lettre in c:
        if lettre != l:
            c_suppr = c_suppr + lettre
    return c_suppr
            
