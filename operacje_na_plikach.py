# podstawowa metoda wczytywania plików (mniej preferowana)
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.txt'  # uwaga na podwójny '\\' i r'' - charakterstyczne dla dodawania ścieżek na Windows
f = open(path, 'w')  # tworzy plik od nowa ('w' - write)
# f.write('Hello World' + '\n')
f.write('Hello World')
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.txt'
f = open(path, 'a')  # dodaje do pliku nowa tresc - 'a' - append
f.write('last message' + '\r')  # '\t', '\r' , '\n' - najwazniejsze 'escape characters', '\n' - nowa linia (poniżej), '\t' - tabulacja, '\r' - nowa linia przy skasowaniu tego co na lewo od znaku
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.bin'
f = open(path, 'wb')  # tworzy plik binarny od nowa ('wb' - write binary)
f.write(bytes('aaaa', 'utf-8'))
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.txt'
f = open(path, 'r')  # 'r' - read - czytanie
print(f.readlines())
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.txt'
f = open(path, 'r')  # read - czytanie
l = f.readlines()   # tworzenie listy kolejnych linijek pliku
for el in l:        # iteracja po elementach listy
    print(el)
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.txt'
f = open(path, 'r')  # read - czytanie
print(f.readline(2))  # argument readline(x) - x - liczba znaków do wyświetlenia od początku pliku
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.txt'
f = open(path, 'r')  # read - czytanie
x = f.read()        # czytanie całości pliku
print(x)
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.bin'
f = open(path, 'rb')  # 'rb' - read binary - czytanie binarnego pliku
print(f.read())       # .read() - czytanie całości na raz
f.close()

###########################################################

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.txt'
with open(path, 'r') as f:
    for line in f:      # directly iterating generator (f)
        print(line)

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'plik.txt'
with open(path, 'r') as f:
    print(f.read())

###########################################################

string = ' afiewpj aoe ap ar a a aa'
print(string.replace('a', '$').replace('p', '£'))   # zamiana znaków

# stworzmy plik o tresci:
"""
Hello WorldHello Python!!!
New message,
another message, last message...
"""
# usunmy z niego znaki specjalne ('!', ',', '.') - sugestia read- traktujemy plik jako calosc

# 1 stworz plik, ktory bedzie mial powyzsza tresc
# 2 odczytaj (sprawdz) przez Pythona czy dobrze jest stworzony
# 3 zmodyfikuj plik usuwajac znaki specjalne ('!', ',', '.')

string = """Hello WorldHello Python!!!
            New message,
            another message, last message..."""
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'file.txt'
with open(path, 'w') as f:
    f.write(string)

with open(path, 'r') as f:
    l = f.readlines()
    print(l)
    print(len(l))

x = x.replace(',', '').replace('.', '').replace('!', '')

with open(path, 'w') as f:
    f.write(x)

##############################################################################

# stworzmy plik o tresci:
"""
Hello, World. Hello, Python!!!
New message!!
another message, last message...
"""
# usunmy z pierwszej linijki tylko ','
# z drugiej linijki '!'
# z trzeciej linijki usunmy '.'

# 1 stworz plik, ktory bedzie mial powyzsza tresc
# 2 odczytaj (sprawdz) przez Pythona czy dobrze jest stworzony
# 3 zmodyfikuj plik usuwajac znaki specjalne ('!', ',', '.')

string = """Hello WorldHello Python!!!
New message,
another message, last message...
"""
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'file.txt'
with open(path, 'w') as f:
    f.write(string)

########

with open(path, 'r') as f:
    l = f.readlines()
    print(l)

i = -1
with open(path, 'w') as f:
    for el in l:
        i = i + 1
        if i == 0:
            print('0')
            x = el.replace(',', '')
            f.write(x)
        elif i == 1:
            y = el.replace('!', '')
            f.write(y)
        elif i == 2:
            z = el.replace('.', '')
            f.write(z)

#############################

## rozwiazanie Marcina:
import string

path = r'c:\Users\piata_m\Downloads\SzkoleniePython\\' + 'plik.txt'
f = open(path, 'w')  # w = tworzy plik od nowa
f.write('Zapis do nowego pliku !!!' + '\n')
f.write('Zapis, do, nowego, pliku !!,' + '\n')
f.close()

f = open(path, 'a')  # a = append, dodaje na koncu pliku
f.write('Dodanie * informacji * do * pliku' + '\r')
f.close()

i = 0
newline = ''

with open(path) as f:
    for line in f:
        i = i + 1
        if i == 1:
            newline = line.replace('!', '#')
        if i == 2:
            newline = newline + line.replace(',', '$')
        if i == 3:
            newline = newline + line.replace('*', '^')

f = open(path, 'w')
f.write(newline)
f.close()

##########################################################
### operacjach na stringach (ale wczesniej podstawy list)

# '\r', '\n'

print("hello \n world")     # pokazanie różnicy między \r i \n
print("hello \r world")
print("hello \r\n world")
print("hello \n\r world")

print(type(range(1, 10)))

lista = [1, 2, 3, 5, 8, 13]

# pierwszy element listy odpowiada zawsze indeksowi zero!! Ostatni indeks to długość listy - 1.
print(lista[0])  # 1
print(lista[5])  # 13

krotka = (1, 2, 3)
print(type(krotka))     # krotka - tuple
print(type(lista))      # lista - list

lista.append(21)

# przykład nadpiywania/updatowania zmiennej lub typowej struktury danych w Pythonie
x = 1
x += 1
x = x + 1
print(x)

#########

x = 3
y = x       # przypisanie wartości x do wartości y

x = x + 2

print(y)    # y dalej pozostaje niezalężne od x, mimo że x został zmieniony - tak działa ogromna większoś zmiennych/typów danych w Pythonie

#########

lista = [1, 2, 3, 5, 8, 13]

lista2 = lista      # przypisanie wartości listy2 do listy

lista.append(21)    # modyfikacja listy

print(lista2)       # lista2, chociaż nie zmieniona bezpośrednio, zmienia się wraz ze zmianą listy do której zostałą przypisana (listy są wyjątkiem!)

############


lista = [1, 2, 3, 5, 8, 13]

lista2 = lista.copy()   # aby uniknąć zamimeszania i uniezlażnić listę2 od listy, musimy skopiować za pomocą .copy()

lista.append(21)

print(lista2)       # wynik niezależny od listy

########################

lista = [1, 2, 3, 5, 8, 13]

lista = lista.append(21)  # tak nie postepowac z listami!!!
print(lista)              # w efekcie otrzymują wartość None - kolejny wyjątek

########################

lista = [1, 2, 3, 5, 8, 13]

lista.append(21)  # tak postepowac z listami!!! Bez przypisywania jak w przypadku innych zmiennych, np x=x+1
print(lista)

#######################   Trzy rodzaje iteracji po listach

lista = [1, 2, 3, 5, 8, 13]

for i in range(0, 6):
    print(lista[i])

for el in lista:
    print(el)

for i, el in enumerate(lista):
    print(i, el)

###################################

import time
                                # porównanie wydajności w przypadku iteracji po indeksie, wartości oraz indeksie+wartości z enumerate
s1 = time.time()
lista = [i for i in range(1, 10000001)]         # list składana
e1 = time.time()
print('lista skladana - czas egzekucji', e1 - s1)

length = len(lista)

s1 = time.time()
for i in range(0, length):
    element = lista[i]
e1 = time.time()
print('lista w petli po indeksie - czas egzekucji', e1 - s1)

s1 = time.time()
for el in lista:
    element = el
e1 = time.time()
print('lista w petli po elemencie - czas egzekucji', e1 - s1)

s1 = time.time()
for i, el in enumerate(lista):
    element = el
    index = i
e1 = time.time()
print('lista w petli po elemencie i indeksie z uzyciem enumerate - czas egzekucji', e1 - s1)

######################################################################

#
# Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.

lista = []      # typowy sposób tworzenia listy (pustej)
# lista = list() # alternatywna werja tworzenia listy
for i in range(1, 11):
    lista.append(2 ** i)

for el in lista:
    print(el)

#################

for i in range(0, 10):
    print(lista[i])

######################################################################

# Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik
# line.strip()

string = """Hello WorldHello Python!!!

New message,

another message, last message...


"""
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'file_empty_lines.txt'
f = open(path, 'w')
f.write(string)
f.close()

with open(path, 'r') as f:
    l = f.readlines()  # to jest lista
    print(l)

# if line.strip(): # sprawdza czy dana linia jest pusta

print('    \n'.strip())
print('     hello world      bla        '.strip().strip())
print('\n'.strip())
# l.remove()


path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\' + 'file_empty_lines.txt'
with open(path, 'r') as f:
    l = f.readlines()  # to jest lista
    print(l)
    for line in l:
        if line.strip():  # sprawdza czy dana linia jest pusta
            print(line.strip())

#######################

string = 'byle jaki string z roznymi  - literami Duzymi I Malymi'

print(string.count('i'))    # liczenie małych 'i'
print(string.count('I'))    # liczenie dużych 'I'

print(string.upper())       # podniesienie wszystkich liter do dużych
print(string.lower())       # zmniejszenie wszystkich liter do malych

print(string.lower().count('i'))

print(string.split())       # dzielenie stringów z defaultowym spóknikiem (split()) - spacją. W efekcie otrzymujemy listę wyrazów
print(string.split('-'))    # dzielenie stringów ze specificznym spójnikiem, w tym przypadku '-'

# '-' in string
# 1 in [1,2,3,4]


# Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego
# podanego przez użytkownika w pliku którego nazwę również poda użytkownik.

fraza = input('podaj szukana fraze')
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\plik.txt'
counter = 0
with open(path, 'r') as file:
    for line in file:
        counter = counter + line.lower().count(fraza.lower())   # lower() stanowi ujednolicenie rozmiaru liter, żeby podana fraza nie zależała od wielkości liter
print(counter)



# odczytaj element 'x' z podanej listy.
# odczytaj wszystkie elementy wewnaatrz list zagniezdzonych (wewnatrz list, ktore sa w liscie):
# lista = [1, 2, 3, 5, 8, 13, 21, [34], [52, 'x', 0]]  . Zakładamy, że nie wiemy który element listy jest  listą.
# innymi słowy, chcemy odczytać 34, 52, 'x', 0 nie wiedząc nic o ich położeniu

print(type('a'))
print(type([1,2,3]))
print(str(type([1,2,3])) == "<class 'list'>")   # sprawdzenie czy dany element ([1,2,3]) jest listą


lista = [1, 2, 3, 5, 8, 13, 21, [34], [52, 'x', 0]]

for el in lista:
    if type(el) == type([]):    # inny sposób na sprawdzenie czy dany element jest listą (lepszy i i prostszy)
        for el2 in el:
            print(el2)

########  modyfikacja zadania, zeby wydrukować indeksy - głównej i wewnętrznej listy (jeśli istnieje)
# indeks glownej listy, indeks listy wewnetrznej (lub brak), wartosc
# 0 , 'brak indeksu wewnetrzeno', 1
# 1, 'brak indeksu wewnetrznego', 2
# ...
# ...
# 7, 0, 34
# 8, 0, 52
# 8, 1, 'x'
# 8, 2, 0
# for i, el in enumerate(lista):


lista = [1, 2, 3, 5, 8, 13, 21, [34], [52, 'x', 0]]

for i, el in enumerate(lista):
    if type(el) == type([]):
        for j, el2 in enumerate(el):
            print(i, j, el2)
    else:
        print(i, 'brak indeksu wewnetrznego', el)

##########################################################

## alternatywne rozwiazanie od Marcina:

lista = [1,2,3,['x','y','z'],4,['a1','a2','a3'],5]
c1 = 0
c2 = 0
for i in lista:
    if str(type(i)) == "<class 'list'>": #type(i) == type([])
        jLista = i
        for k in jLista:
            print(str(k)+', ['+str(c1)+', '+str(c2)+']')
            c2 = c2 + 1
    else:
        print(str(i)+', ['+str(c1)+']')
    c1 = c1 + 1
    c2 = 0

##########################################################

l = [0,3,8,9,3,4,2,1]
l.sort()    # sortowanie listy w naturalnym (rosnącym) porządku
l.reverse()     # odwrócenie kolejności elementów w liście
print(l)

l = [0,3,8,9,3,4,2,1]
l = sorted(l, reverse=True)     # inny sposób na posortowanie listy i odwrócenie kolejności za jednym razem. Zwróćmy uwagę na to, że tu jest przypisanie l = funkcja(l),
                                # w przypadku funkcji należących do listy, np l.funkcja() przypisanie daje w rezultacie l = None
print(l)

from operator import itemgetter     # przydatny operator do sortowania po danym elemencie list/krotki wewnętrznej

lista = [[1, 'banan'], [3, 'ananas'], [2, 'cytryna'] ]

lista = sorted(lista, key=itemgetter(0))  # sortujemy po pierwszej wartości (zerowym indeksie) , tzn: 1,2,3
lista = sorted(lista, key=itemgetter(1))  # sortujemy po drugiej wartości (pierwszym indeksie), tzn: ananas, banan, cytryna

l = [0,3,8,9,3,4,2,1,1,1]
print(l.count(1))       # zliczanie wystąpienie danego elementu w liście (1)

l.insert(5, 2999) #dodanie elementu 2999 na pozycji indeksu = 5
l.pop(5)    # usunięcie elementu o indeksie 5
print(l)

l.remove(9)     # usuniecię elementu o wartości 9
l.remove(1)     # usunięcie elementu o wartości 1 - nie usuwa to jednak wszystkich wartości 1 z listy, tylko pierwszy jaki napotka

l.remove('x')   # usuniecie elementu o wartości 'x'

suma_list = l + lista   # tworzenie nowej listy za pomocą dodania dwóch istniejących list (wymaga to stworzenia nowej zemiennej - suma_list)

l.extend(lista)         # rozszerzenie obecnej listy o drugą listę - nie wymaga tworzenia nowej zmiennej jak w przypadku powyżej

l = [0,3,8,9,3,4,2,1,1,1]
l.append(lista)         # dodwanie listy do listy stworzy element listy będący listą


# Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
# potęgi mają być w zakresie [-1, -10]

lista = []
for i in range(-10,0):
    print(i, 2**i)
    lista.append([i, 2**i])

print(lista)

# alternatywnie:

lista = []
for i in range(1, 11):
    print(i, 2**(-i))
    lista.append([-i, 2**(-i)])

print(lista)

# Następnie posortuj listę za pomocą : a) indeksu b) potęgi c) wartośi potęgowania

final_list = []   # [   [0,-1,0.5], [1,-2, 0.25] ...]
for i, el in enumerate(lista):
    el.insert(0, i)

sorted_by_index = sorted(lista, key=itemgetter(0))
sorted_by_power = sorted(lista, key=itemgetter(1))
sorted_by_result = sorted(lista, key=itemgetter(2))

###################################################
### rozwiazanie w wersji Marcina:

nlista = []
nPodLista = []
iLicznik = 0
for i in range(-10,0):
    nPodLista.append(iLicznik)
    nPodLista.append(i)
    nPodLista.append(2**i)
    nlista.append(nPodLista)
    nPodLista = []
    iLicznik = iLicznik + 1

nlista = sorted(nlista, key=itemgetter(0))
print(nlista)
nlista = sorted(nlista, key=itemgetter(1))
print(nlista)
nlista = sorted(nlista, key=itemgetter(2))
print(nlista)


##################################################

# wersja łatwiejsza (nieobowiązkowo)
# Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.


# Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.   # random.uniform() lub random.randrange()
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo dodać dwie listy (+))

import random as rn

nlista1 = []
nlista2 = []
for i in range(1,11):
    nlista1.append(rn.randrange(1,11))
    nlista2.append(rn.randrange(1,11))

nlista = nlista1 + nlista2
print(nlista)
nlista1.extend(nlista2)
print(nlista1)


##### z wymiernymi:
nlista1 = []
nlista2 = []
for i in range(1,11):
    nlista1.append(rn.uniform(1,11))
    nlista2.append(rn.uniform(1, 11))

nlista = nlista1 + nlista2
print(nlista)
nlista1.extend(nlista2)
print(nlista1)

### test probablistyczny:
for i in range(1,1000001):
    x = rn.randrange(1, 2)
    if x == 2:
        print(x)
        break
print('zawsze 1')

# wynika, ze 2 nigdy nie wystepuje wiec musimy zwiekszac o 1 prawa strone range (przedział prawostronnie otwarty)


lista_skladana = [i for i in range(0,10)]
### rownowaznosc tego zapisu:
for i in range(0,10):
    lista_skladana.append(i)

lista_skladana = [str(i) for i in range(0,10)]  # przykładowa operacja na tworzeniu listy składanej (zamiana int na string)

# Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych pierwiastków liczby 2

lista_skladana = [2**(1/i) for i in range(1,11)]
print(lista_skladana)


l  = [i + j for i in range(0,10) for j in range(0,10)]
# Korzystając z list składanych (zagniezdzonych) wygeneruj tabliczkę mnożenia. Każdy element będzie listą z 3 wartościami.
# Pierwszy i drugi element tej podlisty to liczby, które mnożymy, a trzeci element to wynik mnożenia.

# wstep - tradycyjnie

l = []
for i in range(1,11):
    for j in range(1,11):
        l.append([i,j,i*j])

# z listą składaną:

l  = [ i,j,i*j] for i in range(1,11) for j in range(1,11)]

########
### .upper() .lower()
'filip waszkiewicz'.title()         # funkcja title podnosi pierwszą literę każdego słowa
'Blockchain in the use of social media'.title()     # niestety też podnosi słowa typu in, of, the itd - co nie jest wskazane w tytułach
'COKOLWIEK'.title()

l = 'filip waszkiewicz'.title().split()

s = '@'.join(['Filip', 'Waszkiewicz'])      # join będący odwrotnością split - split tworzy litę ze stringa, join tworzy string z listy
print(s.split('@'))
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane.txt'

import os
f = os.path.join(path,filename)     # bardziej profesjonalny sposób łączenia ścieżek (szczególnie przydatny na systemach Windows)

# Napisz program który z pliku dane.txt (lub dane.csv) wyświetli powiekszone imiona i nazwiska oraz wzrost i masę
# 1 kolumna - wzrost w m (idac od lewej)
# 2 kolumna - masa w kg
# 3 kolumna - wiek
# 4 kolumna - imie i nazwisko
# print( imie i nazwisko, wzost, masa)

path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane.csv'

import os
filename = os.path.join(path,filename)


with open(filename, 'r') as f:
    for line in f:
        lista = line.split(',')
        wzrost = lista[0]
        masa = lista[1]
        full_name = str(lista[3]).upper()
        print(wzrost, masa, full_name)

# Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.txt -- nieobowiązkowo - możemy zrobić normalnie
# w taki sposób by linie oczyścic z bialych znaków (pozbyc się '\n' oraz spacji - rozdzielić imie i nazwisko, tak, żeby było w oddzielnych polach listy)
# i rozbić na listy.
# Każdy z elementów listy sam powinien byc listą. Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy  linia po linii.
# przykład: [[wzrost1, waga1, wiek1, imie1, nazwisko1], [wzrost2, waga2, wiek2, imie2, nazwisko2], .... ]
# lista_list

### Rozwiazanie Marcina:
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane.csv'

import os
filename = os.path.join(path,filename)
ListaKoncowa = []
with open(filename) as f:
    for line in f:
        lista = line.split(',')
        Wzrost = lista[0].strip()
        Masa = lista[1].strip()
        Wiek = lista[2].strip()
        ImieNazwisko = lista[3].upper().split(' ')  # split()
        Imie = ImieNazwisko[0].strip()
        Nazwisko = ImieNazwisko[1].strip()
        NowaLista = [Wzrost, Masa, Wiek, Imie, Nazwisko]
        print(NowaLista)
        ListaKoncowa.append(NowaLista)
        NowaLista = []

# tutaj bedzie kod

for el in ListaKoncowa:
    print(el)


#Z pliku dane.txt. Dane posortuj po imionach i wyswietl linia po linii na konsoli.
# wskazówka: itemgetter

path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane.csv'

import os

filename = os.path.join(path, filename)
ListaKoncowa = []
with open(filename) as f:
    for line in f:
        lista = line.split(',')
        Wzrost = lista[0].strip()
        Masa = lista[1].strip()
        Wiek = lista[2].strip()
        ImieNazwisko = lista[3].upper().split(' ')  # split()
        Imie = ImieNazwisko[0].strip()
        Nazwisko = ImieNazwisko[1].strip()
        NowaLista = [Wzrost, Masa, Wiek, Imie, Nazwisko]
        print(NowaLista)
        ListaKoncowa.append(NowaLista)
        NowaLista = []

ListaKoncowa = sorted(ListaKoncowa, key = itemgetter(3))

for el in ListaKoncowa:
    print(el)

# Z pliku dane.txt: Zapytaj użytkownika o frazę, a następnie wyświetl frazę z numerem linii oraz linią, w której znajduję się ta fraza
# wzkazówka: in , ewentualnie ' '.join(list)

path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'dane.csv'
import os
filename = os.path.join(path, filename)
fraza = input('podaj poszukiwaną frazę')
fraza = fraza.lower()
nr_linii = 1
with open(filename, 'r') as file:
    for line in file:
        if fraza in line.lower():
            print(fraza, nr_linii, line )
        nr_linii += 1


#####################################








# to na pozniej
# Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
#  poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka
#  odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
#  i  jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.


# (musze omowic biblioteke os)
