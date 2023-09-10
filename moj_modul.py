"""
Ten moduł dostarcza podstawowych funkcji do przywitania i arytmetyki.
"""

def powitanie(imie):
    """
    Zwraca wiadomość powitalną.
    """
    return f"Witaj, {imie}!"

def dodaj(a, b):
    """
    Zwraca sumę dwóch liczb.
    """
    return a + b

zmienna = "zmienna w module"

def oblicz_bmi(wzrost, masa):
    return masa / (wzrost/100)**2


