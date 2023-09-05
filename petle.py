

for x in range(1, 21):              # przykład pętli for z użyciem dwóch oddzielnych instrukcji warunkowych, z których tylko pierwszy jest spełniony za sprawą 'break'
    print(x)
    if x < 18 or x > 64:
        print('osoba w wieku nie-pracującym')
        break
    ###### nastepny warunek
    if x < 18:
        print('osoba niepelnoletnia')



for x in range(1, 100):     # tutaj tak samo - 'break' wyrzuca nas z pętli
    print(x)
    if x == 18:
        print('pierwszy break')
        break
    ###### nastepny warunek
    if x == 18:
        print('drugi break')
        break

for x in range(1, 30):          # dwa oddzielne warunki bez 'break' - oba wyświetlone
    print(x)
    if x == 18:
        print('18-nastka!')
    ###### nastepny warunek
    if x == 18:
        print('18-nastka')


for x in range(1, 30):      # przykład 'continue' - przejście do następnej iteracji
    print(x)
    if x == 18:
        print('18-nastka!')
        continue
    ###### nastepny warunek
    if x == 18:
        print('18-nastka')


# Wyświetl 20 kolejnych potęg liczby 2  # 1-20

# 2**1 = 2
# 2**2 = 4
# 2**3 = 8
# 2**4 = 16
# 32
# 64
# 128
#
#
# 2**i

for i in range(1, 21):
    print(2**i)

# Wydrukuj co 2 liczbę z zakresu 1-50   #

for i in range(1, 26):      # parzyste
    print(2*i)

for i in range(1, 26):      # nieparzyste
    print(2*i-1)

########################################
# % - modulo - reszta z dzielenia

for i in range(1, 51):  # to samo za pomocą operatora 'modulo'
    if i % 2 == 0:  # parzyste
        print(i)

for i in range(1, 51):
    if i % 2 == 1:  # nieparzyste
        print(i)

########################################

for i in range(1, 51, 2):  # inny sposób z wykorzystaniem trzeciego argumentu 'range'
    print(i)

########################################

# Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#   parzysta czy nieparzysta

for i in range(1, 101):
    a = 'parzysta'
    b = 'nieparzysta'
    if i % 2 == 1:
        print(i, b)
    elif i % 2 == 0:
        print(i, a)

############### nieskonczona petla
while True:
    print('info')


############### nieskonczona petla z przerwa - nie rekomendowane
i=0
while True:
    i = i + 1
    #i += 1
    print(i)
    if i == 18:
        break

############### petla while z ograniczeniem:

i = 0
while i <= 18:
    print(i)
    i += 1


# Napisz korzystajac z petli while program który wyświetli
#  10 kolejnych potęg liczby 2.
# moja wersja: od 1 do 10 wlacznie

i = 1
while i <11:
    print(2**i)
    i = i + 1


# 2**i , i<wartosc uzytkownika
#Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość potęgi nie przekroczy wartości podanej przez użytkownika

potega_max = int(input('podaj wartość potęgi, ktorą ma nie być przekroczona'))
i = 0
while i < potega_max:   # ograniczenie 'potega_max' wiąże się z kolejnością drukowania i zwiększania indeksu 'i'
    print(i, 2**i)
    i  = i + 1

potega_max = int(input('podaj wartość potęgi, ktorą ma nie być przekroczona'))
i = 0
while i < potega_max - 1:
    i  = i + 1
    print(i, 2 ** i)

# 2**i , 2**i < wartosc uzytkownika
#Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość wyniku potegowania nie przekroczy wartości podanej przez użytkownika

iWartoscPotegi = int(input('Podaj max wartosc potegi liczby 2 do której to mam liczyć wynik: '))
iPetlaIteracjaMax = 0
while 2**iPetlaIteracjaMax <= iWartoscPotegi:
    print(2**iPetlaIteracjaMax)
    iPetlaIteracjaMax = iPetlaIteracjaMax + 1

########################################

 # Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
 #  - kwotę lokaty
 #  - oprocentowanie w skali roku # 0.05, 5% -> 5 -- trzeba podzielic przez 100
 #  - ilość miesięcy na jaką zakladamy lokatę
 #  Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
 #  oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
 #  Kapitalizacja comiesięczna

 #r = 0.05

# kwota1 = kwota0*(1+r/12)
# kwota2 = kwota1*(1+r/12)
# kwota3 = ...
# ....
# ..

#r = 5

# kwota1 = kwota0*(1+r/(100*12))

# można sprawdzić zgodność dla n-tego miesiąca zgodnie ze wzorem: https://pl.wikipedia.org/wiki/Kapitalizacja_odsetek

kwota0 = float(input('podaj kwotę lokaty'))
r = float(input('podaj oprocentowanie w skali roku w %'))/100
miesiace = int(input('podaj  ilość miesięcy na jaką zakladamy lokatę'))


kwota = kwota0
for i in range(1, miesiace + 1):
    kwota = kwota*(1+ r/12)
    print('kwota po miesiacu', i, round(kwota, 2))


kwota_teoretyczna = kwota0*((1+ r/12)**miesiace)
print('kwota ze wzoru', round(kwota_teoretyczna, 2))


import math
print(math.floor(2.9))

print('{:.0}'.format(2.51))

###################

# Napisz program bedacy licznikiem bomby, który korzystając z pętli while
# bedzie odliczal od wartosci podanej przez uzytkownika do 0 po czym wypisze "kaboom!"

import time

start = time.time()
for i in range(0,500000):
    pass
    #time.sleep(0.5)
    print(i)
end = time.time()
print(end-start)

############################

liczba = int(input('podaj liczbe do odliczania'))

while liczba > 0:
    print(liczba)
    time.sleep(0.5)
    liczba -= 1

print('kaboom!')

############################

liczba = int(input('podaj liczbe do odliczania'))

while liczba > -100:
    print(liczba)
    time.sleep(0.5)
    liczba -= 1
    if liczba == 0:
        print('kaboom!')
        break

############################

import random as rn

rn.random()
rn.randrange(0,100)

# Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci wiekszej od wartosci podanej przez uzytkownika
