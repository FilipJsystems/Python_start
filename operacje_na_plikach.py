


path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.txt'
f = open(path, 'w') # tworzy plik od nowa
#f.write('Hello World' + '\n')
f.write('Hello World')
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.txt'
f = open(path, 'a') # dodaje do pliku nowa tresc - append
f.write( 'last message'+ '\r')   # '\t', '\r' , '\n' - najwazniejsze
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.bin'
f = open(path, 'wb') # dodaje do pliku nowa tresc - append
f.write(bytes('aaaa', 'utf-8'))   # '\t', '\r' , '\n' - najwazniejsze
f.close()


path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.txt'
f = open(path, 'r') # read - czytanie
print(f.readlines())
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.txt'
f = open(path, 'r') # read - czytanie
l = f.readlines()
for el in l:
    print(el)
f.close()


path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.txt'
f = open(path, 'r') # read - czytanie
print(f.readline(2))
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.txt'
f = open(path, 'r') # read - czytanie
x = f.read()
print(x)
f.close()

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.bin'
f = open(path, 'rb') # read binary - czytanie binarnego
print(f.read())
f.close()

###########################################################

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.txt'
with open(path, 'r') as f:
    for line in f:
        print(line)

path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'plik.txt'
with open(path, 'r') as f:
    print(f.read())

###########################################################

string = ' afiewpj aoe ap ar a a aa'
print(string.replace('a', '$').replace('p', '£'))


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
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'file.txt'
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
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'file.txt'
with open(path, 'w') as f:
    f.write(string)

########

with open(path, 'r') as f:
    l = f.readlines()
    print(l)


i = -1
with open(path, 'w') as f:
    for el in l:
        i = i+1
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
path = r'c:\Users\piata_m\Downloads\SzkoleniePython\\'+'plik.txt'
f = open(path,'w') # w = tworzy plik od nowa
f.write('Zapis do nowego pliku !!!'+'\n')
f.write('Zapis, do, nowego, pliku !!,'+'\n')
f.close()

f = open(path,'a') # a = append, dodaje na koncu pliku
f.write('Dodanie * informacji * do * pliku'+'\r')
f.close()

i = 0
newline = ''

with open(path) as f:
    for line in f:
        i = i + 1
        if i == 1:
            newline = line.replace('!','#')
        if i == 2:
            newline = newline + line.replace(',', '$')
        if i == 3:
            newline = newline + line.replace('*','^')

f = open(path,'w')
f.write(newline)
f.close()

##########################################################
### operacjach na stringach (ale wczesniej podstawy list)

#'\r', '\n'

print("hello \n world")
print("hello \r world")
print("hello \r\n world")
print("hello \n\r world")


print(type(range(1,10)))

lista = [1,2,3,5,8,13]

print(lista[0]) # 1
print(lista[5]) # 13

krotka = (1,2,3)
print(type(krotka))
print(type(lista))

lista.append(21)

x = 1
x +=1
x = x + 1
print(x)

#########

x = 3
y = x

x = x + 2

print(y)

#########

lista = [1,2,3,5,8,13]

lista2 = lista

lista.append(21)

print(lista2)

############


lista = [1,2,3,5,8,13]

lista2 = lista.copy()

lista.append(21)

print(lista2)

########################

lista = [1,2,3,5,8,13]

lista = lista.append(21)   # tak nie postepowac z listami!!!
print(lista)

########################

lista = [1,2,3,5,8,13]

lista.append(21)   # tak postepowac z listami!!!
print(lista)

#######################

lista = [1,2,3,5,8,13]

for i in range(0,6):
    print(lista[i])

for el in lista:
    print(el)


for i, el in enumerate(lista):
    print(i, el)

###################################

import time

s1 = time.time()
lista = [i for i in range(1,10000001)]
e1 = time.time()
print('lista skladana - czas egzekucji', e1 - s1)


length = len(lista)

s1 = time.time()
for i in range(0,length):
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

lista = []
#lista = list() # alternatywna werja tworzenia listy
for i in range(1,11):
    lista.append(2**i)

for el in lista:
    print(el)

#################

for i in range(0,10):
    print(lista[i])

######################################################################

#Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego którego nazwę poda użytkownik
# line.strip()

string = """Hello WorldHello Python!!!

New message,

another message, last message...


"""
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'file_empty_lines.txt'
f = open(path,'w')
f.write(string)
f.close()


with open(path, 'r') as f:
    l = f.readlines()  # to jest lista
    print(l)

#if line.strip(): # sprawdza czy dana linia jest pusta

print('    \n'.strip())
print('     hello world      bla        '.strip().strip())   # resultat: 'hello'
print('\n'.strip())
#l.remove()


path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'file_empty_lines.txt'
with open(path, 'r') as f:
    l = f.readlines()  # to jest lista
    print(l)
    for line in l:
        if line.strip():  # sprawdza czy dana linia jest pusta
            print(line.strip())


# path = r'C:\Users\localadmin\PycharmProjects\pythonProject\\'+ 'file_empty_lines.txt'
# with open(path) as f:
#     l = f.readlines()
#     print(l)
#     for i in l:
#         if not i.strip():
#             l.remove(i)
# print(l)
#
# for el in l:
#     print(el)

#######################

string = 'byle jaki string z roznymi  - literami Duzymi I Malymi'

print(string.count('i'))
print(string.count('I'))

print(string.upper())
print(string.lower())

print(string.lower().count('i'))

print(string.split())
print(string.split('-'))

# '-' in string
# 1 in [1,2,3,4]


# Napisz program który zliczy ilość wystąpień małej lub dużej wersji ciagu tekstowego
# podanego przez użytkownika w pliku którego nazwę również poda użytkownik.

fraza = input('podaj szukana fraze')
path = r'C:\Users\localadmin\PycharmProjects\pythonProject\plik.txt'
counter = 0
with open(path, 'r') as file:
    for line in file:
        counter = counter + line.lower().count(fraza.lower())
print(counter)


# Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.


# to na jutro (musze omowic biblioteke os)
# Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
#  poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#   inie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka
#     odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
#   i  jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.