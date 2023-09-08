# Deklarowanie funkcji

# def nazwa_funkcji():
#     # treść funkcji

# przykład

def powitanie():
    print("Hello!")

global a
a = 2

def powitanie2():
    if a > 1:
        print("Hello!")
    else:
        print('lipa')

powitanie()

# Parametry funkcji

def mnozenie(x, y):
    return x*y

print(mnozenie(3,4))

def mnozenie_z_potega(x, y, z=1, b = 0):   # parametr opcjonalny z defaultową wartością
    result = (x * y)**z + b
    return result


print(mnozenie_z_potega(3,4))           # 3*4 do potegi 1 + 0
print(mnozenie_z_potega(3,4,2))         # 3*4 do potegi 2 + 0
print(mnozenie_z_potega(3,4,2,1))       # 3*4 do potegi 2 + 1
print(mnozenie_z_potega(2,2, b = 4))    # 2*2 do potegi 1 + 4

# Wyrażenia Lambda
# funkcje lambda to funkcje anonimowe, tworzone na szybko - mogą mieć wiele arguementów ale tylko jednen rezultat
# lambda argument(y) : wyrażenie

kwadrat = lambda x: x * x
print(kwadrat(5))

def kwadrat2(x):    # odpowiednik
    return x*x


sumowanie = lambda x, y : x + y
print(sumowanie(12,15))
print(sumowanie('x', 'y'))

# funkja jako argument ########################################

def wykonaj_funkcje(funkcja, wartosc):
    return funkcja(wartosc)

print(wykonaj_funkcje(kwadrat, 5))  # przyjmuje funkje lambda 'kwadrat' jako argument


def wykonaj_funkcje_dwuargumentowa(funkcja, wartosc1, wartosc2):
    return funkcja(wartosc1, wartosc2)
print(wykonaj_funkcje_dwuargumentowa(mnozenie,3, 4))  # przyjmuje funkje mnozenie z dwoma argumentami


suma = lambda x: x + x
def wykonaj_funkcje_wieloargumentowa(funkcja,*args):
    for arg in args:
        print(funkcja(arg))

print(wykonaj_funkcje_wieloargumentowa(kwadrat,3, 4,5,6))  # None z powodu zwracania
wykonaj_funkcje_wieloargumentowa(kwadrat,3, 4,5,6)          # nie ma None bez printu

podwojenie = lambda x: x + x
kwadrat = lambda x: x * x

def wykonaj_funkcje_wieloafunkcyjna(wartosc,*funkcs):
    for f in funkcs:
        wartosc = f(wartosc)
    return wartosc


print(wykonaj_funkcje_wieloafunkcyjna(3, kwadrat, podwojenie ))  # najpierw podnosi do kwadratu, później podwaja

# Funkcja w funkcji # funkja jako argument ########################################


suma = lambda x: x + x

def funkcja_zewnetrzna(x):
    def funkcja_wewnetrzna(y):
        return y * y
    return funkcja_wewnetrzna(x) + 2

result = funkcja_zewnetrzna(5)
print(result)  # To wydrukuje 27 (bo 5*5 + 2 = 27)

# Dokumentowanie funkcji  ########################################


def dodaj(a, b):
    """
    opis działania funkcji i parametrów
    """
    return a + b

print(dodaj.__doc__)

# albo

help(dodaj)

# map i filter ########################################

def kwadrat(n):
    return n * n

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

liczby_podniesione_do_kwadratu = list(map(kwadrat, liczby))

print(liczby_podniesione_do_kwadratu)  # Output: [1, 4, 9, 16, 25]


# Mamy liste liczb i chcemy uzyskać tylko parzyste liczby ze słownika

def jest_parzysta(n):
    return n % 2 == 0

liczby_parzyste = list(filter(jest_parzysta, liczby))

print(liczby_parzyste)  # Output: [2, 4, 6, 8, 10]


# Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc po przecinku BMI.
# W przypadku pojawienia się wyjątku, wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.



# Napisz funkcję która zwróci pod postacią listy krotek zawartość pliku
# którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
# podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie podane ma przyjac utf-8

