############# krotki - po angielsku tuple

# lista - mutable
# krotka - immutable - niemutowalna, niezmienna

# lista moze sie zmieniac pod wzgledem rozmiaru, elementów, ma sporo funkcji na których można działać
# krotka nie może się zmieniać (może zostać jedynie nadpisana). Prawie nie ma żadnych istotnych funkcji

t = tuple([1, 2, 3, 4]) # tak można zadeklarować krotkę
t = (1, 1, 1, 2, 3, 4)  # tak można zadeklarować krotkę
# t = tuple(1,2,3,4)   # tak nie można deklarować krotki, ponieważ tuple() przyjmuje tylko jeden argument (najlepiej listę)

print(t.count(1))  # liczy ilosc elementow
print(t.index(4))  # to podaje indeks danego elementu (nie element o indeksie)
print(t.index(1))

for el in t:
    print(el)

length = len(t)

t = tuple(i for i in range(0,100))

# Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli

# tuple(rn.randrange(1,11), rn...)   # to nie jest najwygodniejszy sposob
import random as rn

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
l = list(set(l))  # przydatny trick na pozbycie sié dupliaktów w liście.
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
        NowaKrotka = tuple(line.split(','))   # zamieniamy linię (string) na listę (za pomocą split(,)), a następnie listę na krotkę
        ListaKoncowa.append(NowaKrotka)

print(ListaKoncowa)
ListaKoncowa = list(set(ListaKoncowa))      # usuwamy duplikaty z listy
print(ListaKoncowa)

###################
# Przetwórz plik dane.txt (csv) w taki sposób by w efekcie umieścić w pliku output.txt (koniecznie w txt)
# dane z pliku dane.txt wzbogacone o obliczone BMI, bez duplikatów i rozwiązując problem
# podania przecinka w miejsce kropki we wzroście i masie oraz problem z pustymi wierszami.
#

import os
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane.csv'
filename = os.path.join(path, filename)
ListaKoncowa = []
with open(filename) as f:
    string = f.read()                   # zczytujemy cały plik do stringa
    string = string.replace(',','\t')   # zamieniamy przecinek na inny delimeter (tabulator), bo przecinków chcemy użyć zamiast kropek we floatach (sprowadzamy do polskiej notacji)
    lista = string.split('\n')          # rozdzielamy linia po linii
    for line in lista:
        if line.strip():                # jeśli linia nie jest pusta
            lista2 = line.strip().split()       # usuwamy niepotrzebne spacje z lewej i prawej oraz '\n', następnie tworzymy listę za pomocą split()
            bmi = float(lista2[1]) / (float(lista2[0]) ** 2)        # liczymi BMI zanim zamienimy na '.' na ',' - inaczej nie zamieni się na float
            wzrost = lista2[0].replace('.', ',')                # zamieniamy kropki na przecinki (do polskiej notacji)
            bmi  = str(round(bmi, 2)).replace('.', ',')         # zaokrąglamy bmi do 2 miejsc po przecinku
            waga = lista2[1]
            wiek =  lista2[2]
            imie = lista2[3]
            nazwisko = lista2[4]
            name = lista2[3] + ' ' + lista2[4]                       # tworzymy nową zmienną zawierającą imię i nazwisko po spacji
            ListaKoncowa.append((wzrost, waga, wiek, name, bmi))     # dodajemy w postaci krotki do listy

print(ListaKoncowa)

ListaKoncowa = list(set(ListaKoncowa))          # pozbywamy się duplikatów

with open( r'C:\Users\localadmin\PycharmProjects\pythonProject\output.txt', 'w') as f:
    for el in ListaKoncowa:
        string = ';'.join(list(el))+'\n'   ## HIPER-WAZNE - lista do zrobienia join musi składać się z samych elementów string
        f.write(string)

############################

# wstęp do słowników

dic = dict()
dic = {}

dic = {1:2, 'a': ['a', 'b'], (1,2): 'dupa', 3.9: {2,3} }

# kluczami mogą być: stringi, integery, floaty, krotki,   - podstawowe zmienne i elementy niemutowalne
# nie może być kluczem: lista, zbiór/zestaw/set, słownik (dict)  - elementy mutowalne

# wartości - może być zasadniczo każdy typ danych

# klucz musi wyjątkowy - unikalny. Nie mogą być dwa takie same klucze. Dodając do słownika element o kluczu, który już jest nadpiszemy jego wartość

print(dic.values()) # wypisanie wartości
print(dic.keys())  # wypisanie kluczy
print(dic.items()) # wypisanie par key-value

# dic[key] = value
dic['bbb'] = 'cccc'

########

# Stwórz plik ustawienia.txt i umieść w nim poniższe dane
# encoding;utf-8
# timezone;-2
# color;black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości

dic = {}
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'ustawienia.txt'
filename = os.path.join(path, filename)
with open(filename, 'r') as f:
    for line in f:
        lista = line.split(';')
        key = lista[0]
        value = lista[1]
        dic[key] = value.strip()

for el in dic.items():
    print(el)

for key, value in dic.items():
    print(key, value)

#########################################################################
### inne przykłady

dic = {'a':2, 'b':3 }
print(dic)
### usuwanie elementu ze słowników:
del dic['a']
print(dic)

#### sprawdzanie czy element jest w słowniku:
if 'b' in dic:
    print('yes')

if 3 in dic:
    print('yes')
else:
    print('no')     # jak widać, defaultowo sprawdzenie 'in dic' odwołuje się do sprawdzania kluczy

if 'b' in dic.keys():
    print('yes')

if 3 in dic.values():
    print('yes')

dic['c'] = 4
print(dic)

# for i in lista:          #   wydajność obliczeniową liniową = n
#     pass # jakas operacja
#
#
# # dic[el]    # wydajność natychmiastiowa O(1)
#
# for i in lista:
#     for i in lista:
#         for i in lista:     # złożoność n^3

# Wczytaj do słownika dane z pliku dane.txt (csv) tak by kluczem było imię sklejone z nazwiskiem rozdzielone spacja, a pozostałe dane znalazły się w wartości
# jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.
#{'Filip Waszkiewicz': [masa, wzrost... ], ... }
# lista[-1] - ostatni element listy
# lista[0:3] - pozostałe elementy
# lista[:-1] - wszystkie elementy poza ostatnim

import os
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane2.csv'
filename = os.path.join(path, filename)
dic = {}
with open(filename, 'r') as f:
    for line in f:
        lista = line.split(',')
        full_name = str(lista[-1]).strip()
        rest = lista[:-1]
        dic[full_name] = rest

for key, val in dic.items():
    print('klucz:',key, ', wartosc:',val)


###################################################

# Napisz system który zwróci nam ilość wystąpień każdego ze słow w pliku w postaci listy krotek.
# [  (slowo,ilosc_wystapien),(slowo,ilosc_wystapien)   ]. Nazwa pliku ma zostać przekazana przez zmienną.
# Wynik powinien byc posortowany malejąco wg ilosci wystapien

# a) odczytaj wszystkie linie z pliku i rozbij na słowa. Każde ze słów dodaj do listy.
#     Zadbaj o usunięcie po drodze znaków specjalnych czyli kropek, przecinków, wykrzykników etc.



znaki = ['!', ',', '.', '?', '-', ':', ';']  # można dołożyć więcej znaków, potem omówmy regex jeśli starczy czasu
string = 'aaaa!'
for el in znaki:
    string = string.replace(el, '')

import os
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'Pan_Tadeusz.txt'
filename = os.path.join(path, filename)
lista = []
with open(filename, encoding="utf8") as f:   # czasem pojawiają się dziwne charaktery (znaki) i trzeba ustalić  encoding="utf8" (lub inny encoding)
    for line in f:
        string = line.strip()  # pozbywam się pustych linii, niepotrzebnych spacji itd , '\n'
        temp = string.split()  # string zostaje rozdzielona na liste słow
        lista.extend(temp)

len(lista)
unikalne = set(lista)
print(len(unikalne))


 # stwórz słownik i dla każdego słowa w liście sprawdz czy istnieje juz wpis dotyczący tego słowa
 # w słowniku. Jeśli nie ma to dodaj do słownika wpis o kluczu takim jak sprawdzane słowo i wartości 1
 # dla ilości wystąpień. Jeśli takie słowo pojawia się już w kluczach słownika to trzeba zwiększyc wartośc o 1
##  [ ('dzień', 38), (pan,  35) ]
dic = {}
for slowo in lista:
    slowo = str(slowo).lower()   # ujednoliamy do małych liter
    if slowo not in dic.keys():     # jeśli słowa (klucza) nie ma w słowniku, to ustalamy wartość dla klucza = 1 ( bo to pierwszy napotkany taki element)
        dic[slowo] = 1
    else:
        ile = dic[slowo]         # w przeciwnym wypadku musimy pobrać wartość przypisaną do danego słowo-klucza
        ile += 1                 # zwiększyć o jeden
        dic[slowo] = ile         # updatować wartość dla danego klucza

# wskazówka: ListaKoncowa = sorted(ListaKoncowa, key = itemgetter(3))
# posortować
from operator import itemgetter

lista2 = []
for key, val in dic.items():
    lista2.append((key, val))

lista2 = sorted(lista2, key = itemgetter(1), reverse=True)
print(lista2)

#################################################

