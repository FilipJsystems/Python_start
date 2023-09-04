

for x in range(1, 21):
    print(x)
    if x < 18 or x > 64:
        print('osoba w wieku nie-pracującym')
        break
    ###### nastepny warunek
    if x < 18:
        print('osoba niepelnoletnia')



for x in range(1, 100):
    print(x)
    if x == 18:
        print('pierwszy break')
        break
    ###### nastepny warunek
    if x == 18:
        print('drugi break')
        break

for x in range(1, 30):
    print(x)
    if x == 18:
        print('18-nastka!')
    ###### nastepny warunek
    if x == 18:
        print('18-nastka')


for x in range(1, 30):
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

for i in range(1, 26):
    print(2*i)

for i in range(1, 26):
    print(2*i-1)

########################################
# modulo - reszta z dzielenia

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

for i in range(1, 51):
    if i % 2 == 1:
        print(i)

########################################

for i in range(1, 51, 2):
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

############### petla while z ogranizeniem:

i = 0
while i <= 18:
    print(i)
    i += 1


# Napisz korzystajac z petli while program który wyświetli
#  10 kolejnych potęg liczby 2.




# 2**i , i<wartosc uzytkownika
#Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość potęgi nie przekroczy wartości podanej przez użytkownika

# 2**i , 2**i < wartosc uzytkownika
#Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość wyniku potegowania nie przekroczy wartości podanej przez użytkownika










########################################



 # Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
 #  - kwotę lokaty
 #  - oprocentowanie w skali roku
 #  - ilość miesięcy na jaką zakladamy lokatę
 #  Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
 #  oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
 #  Kapitalizacja comiesięczna

