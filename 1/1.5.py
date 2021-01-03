"""Écrire une définition de la fonction fahrenheit_vers_celsius qui convertit une température
t exprimée en degrés Fahrenheit en son équivalent en degrés Celsius.
Rappel : la température t en degrés Fahrenheit équivaut à la température (t − 32) ∗ 5/9 en degrés Celsius.
"""


def fahrenheit_vers_celsius(t: float) -> float:
    return (t - 32) * 5/9


assert fahrenheit_vers_celsius(212) == 100
assert fahrenheit_vers_celsius(32) == 0
assert fahrenheit_vers_celsius(41) == 5

"""Donner une définition de la fonction celsius_vers_fahrenheit qui effectue la conversion
inverse.
"""


def celsius_vers_fahrenheit(t: float) -> float:
    return t * 9/5 + 32

assert celsius_vers_fahrenheit(100) == 212
assert celsius_vers_fahrenheit(0) == 32
assert celsius_vers_fahrenheit(5    ) == 41