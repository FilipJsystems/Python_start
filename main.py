# Zaczynamy szkolenie!

# if __name__ == '__main__': # funkcja main w Pythonie - nie jest konieczna. Zakomentowałem, żeby uniknąć wcięcia


print('Hello World!')

x = 4   # deklaracja zmiennej int (integer - liczby całkowite)
x2 = 2
y = 3.0  # deklaracja zmiennej float (liczby wymierne)
z = '3'  # deklaracja zmiennej string

print('hello' + str(x) )   # ok (str+str)
print(3 +  int(z) )   # ok (int + int)
print(3 + float(z))   # ok (int + float)

# print('hello' + x)   # nie ok! (str+int)

#
#
print('hello', x )   # inny sposób drukowania dwóch wartości - po przecinku
print(x, type(x))    # sprawdzanie typów zmiennych
print(y, type(y))
print(z, type(z))
#
print(x/x2)    # dzielenie zwracające float
print(x//x2)   # dzielenie zwracające int (największą część całkowitą)

#########

# przykład jednego warunku o różnych wynikach

if x >= 3 and x < 4:        # przykład jednego warunku o różnych oddzielnych
    print('liczba x w przedziale domknietym <3,4)')
elif x == 4:
    print('x = 4')
elif x > 4:
    print('x wiekszy od 4')
else:
    print('nie, x poza przedzialem <3,4) i nie jest wiekszy od 4.')

x = input('podaj swoj wiek')   # przykład wprowadzania danych przez użytkownika (domyślnie odczytywana wartość do string)

# Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"

imie = input('podaj swoje imie')
nazwisko = input('podaj swoje nazwisko')
print(f'Witaj, {imie} {nazwisko}')     # inny sposób wyświetlania wartości , równoznaczny z: print('Witaj', imie, nazwisko) lub print('Witaj ' + str(imie) + ' ' + str(nazwisko))

###############

x = 3.7359835
print(f'{x:.3f}')   # przykład zaokrąglania do 3 miejscc po przecinku
#
x = 3.7359835
print(f'{x:.2f}')
#
print(round(x, 2))   # inny sposób zaokrąglania - w tym przypadku do dwóch miejsc po przecinku

###################################

# BMI= masa/(wzrost*wzrost) .
# Napisz program który odbierze od użytkownika jego masę w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

masa = input('podaj swoja mase w kg')
wzrost = input('podaj swoj wzrost w m')

masa = float(masa)
wzrost = float(wzrost)

bmi = masa / (wzrost ** 2)   # '**'  - znak potęgowania
print(bmi)

###################################

# Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#   wyświetlił nam również odpowiedni opis wg skali z Wikipedii.

masa = float(input("Podaj swoją masę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
bmi = masa / (wzrost ** 2)

if bmi < 18.5:
    opis = "niedowaga"
elif bmi >= 18.5 and bmi <= 25.0:
    opis = "pożądana masa ciała"
else:
    opis = "otyłość"

print(f"Twoje BMI wynosi: {bmi:.2f}, co wskazuje na {opis}")
print('Twoje bmi wynosi {:.2f}'.format(bmi))   # jeszcze inny sposób wyświetlania zmiennych liczbowych (float lub int) razem ze stringami, równoważny sąsiednim.
print('Twoje bmi wynosi' + str(round(bmi, 2)))

###################################

x = int(input('podaj wiek'))

# 0---------18-----------------------------64------------

if x < 18 or x > 64:        # suma dwóch zbiorów ze spójnikiem 'lub'
    print('osoba w wieku nie-pracującym')
elif x >= 18 and x <= 64:   # iloczyn (koniunkcja) dwóch zbiorów ze spójnikiem 'i'
print('osoba w wieku pracującym')

# -----0---------18-----------------------------64------------

if x < 18 and x > 0:    # przykład jednej instrukcji warunkowej z trzema możliwymi rezultatami (tylko jeden rezultat się wyświetli)
    print('osoba niepelnoletnia')
elif x >= 18:
    print('osoba pelnoletnia')
else:
    print('bledny input - podaj liczbe wieksza od zera')

# -----0---------18-----------------------------64------------

x = float(input('podaj wiek'))    # przykład dwóch instrukcji warunkowych - mogą wyświetlić się dwa rezultaty
if x < 18 or x > 64:
    print('osoba w wieku nie-pracującym')
###### nastepny warunek
if x <= 18:
    print('osoba niepelnoletnia')
# -----0---------18-----------------------------64------------

x = float(input('podaj wiek'))
if x < 18 or x > 64:
    print('osoba w wieku nie-pracującym')
###### nastepny warunek
elif x <= 18:
    print('osoba niepelnoletnia')

# -----0---------18-----------------------------64------------

# jak nie robic - nie porownywac roznych typów danych
# x = input('podaj wiek')
# if x < 18 or x > 64:  # to daje error bo porównujemy str z int
#     print('osoba w wieku nie-pracującym')
# ###### nastepny warunek
# elif x <= 18:
#     print('osoba niepelnoletnia')

# -----0---------18-----------------------------64------------

x = input('podaj wiek')      # porównanie dwóch stringów - liczy się wtedy kolejność alfabetyczna
if x < '18' or x > '64':
    print('osoba w wieku nie-pracującym')
###### nastepny warunek
elif x <= '18':
    print('osoba niepelnoletnia')

x = input('podaj plec')     # porównanie dwóch stringów na tak lub nie - dużo częściej używane z '==' lub '!=' niż '<' itd.
if x == 'kobieta':
    print('kobieta')
else:
    print('cos innego')

x = input('podaj litera')
if x > 'c':
    print('wiekszy')
else:
    print('mniejszy')

# -------------------------------------------------------------
x = True    # typy logiczne boolean
x = False
x = None

if x == True:
    print('True')
else:
    print('False')


##################################
def f(x):               # przykład wygenerowania zmiennej o wartości None i jej zachowanie
    if x > 18:
        return x


x28 = f(15)    # funkcja nie zwraca nic, więc zmienna 'x28' ma wartość None

if x28 == None:
    print('None')

if x28:
    print('Exists')

if not x28:
    print('Not exists')