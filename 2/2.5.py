from math import sqrt

def v_tetra(a: float, b: float, c: float, d: float, e: float, f: float) -> float:
    """Précondition: a,b,c,d,e,f >= 0
    Cette fonction calcule le volume d'un tétraèdre"""
    x: float = (a**2)+(b**2)-(d**2)
    y: float = (b**2)+(c**2)-(e**2)
    z: float = (a**2)+(c**2)-(f**2)
    p: float = 4*(a**2)*(b**2)*(c**2)
    q: float = (a**2)*(y**2)+(b**2)*(z**2)+(c**2)*(x**2)
    r: float = x*y*z
    return 1/12*sqrt(p-q+r)


assert v_tetra(1, 1, 1, 1, 1, 1) == 0.11785113019775792


def v_tetra_regulier(x: float) -> float:
    return sqrt(2) / 12 * (x**3)


assert v_tetra_regulier(2) == 0.9428090415820635
assert v_tetra_regulier(1) == 0.11785113019775793
