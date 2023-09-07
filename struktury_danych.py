############# krotki - po angielsku tuple

# lista - mutable
# krotka - immutable - niemutowalna, niezmienna

# lista moze sie zmieniac pod wzgledem rozmiaru, elementów, ma sporo funkcji na których można działać
# krotka nie może się zmieniać (może zostać jedynie nadpisana). Prawie nie ma żadnych istotnych funkcji

t = tuple([1, 2, 3, 4]) # tak można zadeklarować krotkę
t = (1, 1, 1, 2, 3, 4)  # tak można zadeklarować krotkę
# t = tuple(1,2,3,4)   # tak nie można deklarować krotki, ponieważ tuple() przyjmuje tylko jeden argument (najlepiej listę)

t.count(1)  # liczy ilosc elementow
t.index(4)  # to podaje indeks danego elementu
t.index(1)

for el in t:
    print(el)

length = len(t)

t = tuple(i for i in range(0,100))

# Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli

# tuple(rn.randrange(1,11), rn...)   # to nie jest najwygodniejszy sposob

t1 = tuple( rn.randrange(1,11) for i in range(0,10) )   # odpowiednik składanej listy dla krotek
t2 = tuple( rn.randrange(11,21) for i in range(0,10) )

t = t1+t2
print(t)
print(len(t))

# Napisz kod ktory wyświetli w postaci listy krotek zawartość pliku dane.txt (lista ma zawierać krotki, a krotka ma mieć tyle elementów ile kolumn/komórek w danym wierszu)
import os
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane.csv'
filename = os.path.join(path, filename)
ListaKoncowa = []
with open(filename) as f:
    for line in f:
        NowaKrotka = tuple(line.split(','))
        print(type(NowaKrotka))
        ListaKoncowa.append(NowaKrotka)
print(ListaKoncowa)

################ Zestawy (sets) - zbiory

x = {}          # dict
print(type(x))  # słownik

x = {1,2,3,4}
print(type(x))  # set (zbiór)

x = {1:2, 2:3}  # słownik (dict)
print(type(x))

# bezpieczna metoda deklaracji zbiorów (zestawów) i słowników - jeżeli są puste

x = set()       # tak tworzymy zbiór pusty
print(type(x))

x = dict()
print(type(x))

####################################

x = (1)
print(type(x)) # dalej int

x = ({1,2,3,4})
print(type(x))  # dalej set (zbiór)

x = ({1:2, 2:3})  # dalej słownik (dict)
print(type(x))

##### wyjaśnienie - krotka 1-elementowa przechodzi natychmiastiowo w ten jeden element
# - nie ma zbyt dużego sensu używac 1-elementowych krotek ponieważ one się nie zmieniaja, więc wartość i tak zostanie ta sama.

x = [1]
print(type(x))  # w tym przypadku jest to lista, ponieważ list jest mutowalna


x = ({1,2,3,4}, {5,6})
print(type(x))          # tutaj już jest krotka (ponieważ ma więcej niż jeden element)


####################### głowna cecha zbiorów - to jest unikalnośc elemntów - z tego względu używa się do deduplikacji

l = [1,1,1,1,2,3,4,5]

print(set(l))

print(l)
l = list(set(l))  # przydatny trick na pozbycie dupliaktów.
print(l)

##### działania na zbiorach:

set1  = set([1,2,3,3,4])
set1 = {1,2,3,3,4}

set2 = {3,4,5,6}

print(set1.intersection(set2))  # część wspólna zbiorów
print(set1 & set2)      #część wspólna zbiorów - inny zapis
print(set1 and set2)  # tak nie robimy bo to nnie ma sensu

print(set1.union(set2))  # suma zbiorów
print(set1 | set2)      # suma zbiorów zbiorów - inny zapis
print(set1 or set2)  # tak nie robimy bo to nnie ma sensu

#   A u B = A + B - A^B
# A \ B = A - A^B
print(set1.difference(set2))  # rożnica zbiorów
print(set1 - set2)      # róznica zbiorów zbiorów - inny zapis

# Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może być mniejsza niż 20 elementów) losowych liczb z zakresu 1-40.
# Wyswietl ich sumę, różnicę i część wspólną

import random as rn
s1 = set(rn.randrange(1,41) for i in range(1,21))
s2 = set(rn.randrange(1,41) for i in range(1,21))

print(s1)
print(s2)
print(s1.union(s2))
print(s1.difference(s2))
print(set1.intersection(s2))

# Zduplikuj jeden z wierszy w pliku dane.txt.
# Napisz kod który zwróci do postaci listy krotek zawartość tego pliku z danymi bez powtórek.
# bez powtórek - czyli z użyciem set

import os
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane.csv'
filename = os.path.join(path, filename)
ListaKoncowa = []
with open(filename) as f:
    for line in f:
        NowaKrotka = tuple(line.split(','))
        ListaKoncowa.append(NowaKrotka)

print(ListaKoncowa)
ListaKoncowa = list(set(ListaKoncowa))
print(ListaKoncowa)

