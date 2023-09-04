# Zaczynamy szkolenie!

# if __name__ == '__main__':


print('Hello World!')

x = 4
x2 = 2
y = 3.0
z = '3'

# print('hello' + str(x) )   # ok
# print(3 +  int(z) )   # ok
# print(3 + float(z))   # ok
#
#
# print('hello', x )   # ok
# print(x, type(x))
# print(y, type(y))
# print(z, type(z))
#
# print(x/x2)
# print(x//x2)

#########

if x >= 3 and x < 4:
    print('liczba x w przedziale domknietym <3,4)')
elif x == 4:
    print('x = 4')
elif x > 4:
    print('x wiekszy od 4')
else:
    print('nie, x poza przedzialem <3,4) i nie jest wiekszy od 4.')

x = input('podaj swoj wiek')

# Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"

# imie = input('podaj swoje imie')
# nazwisko = input('podaj swoje nazwisko')
# print(f'Witaj, {imie} {nazwisko}')
#
# x = 3.7359835
# print(f'{x:.3f}')
#
# x = 3.7359835
# print(f'{x:.2f}')
#
# print(round(x, 2))

###################################

# BMI= masa/(wzrost*wzrost) .
# Napisz program który odbierze od użytkownika jego masę w kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

masa = input('podaj swoja mase w kg')
wzrost = input('podaj swoj wzrost w m')

masa = float(masa)
wzrost = float(wzrost)

bmi = masa / (wzrost ** 2)
print(bmi)

###################################

# Rozbuduj swój program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#   wyświetlił nam również odpowiedni opis wg skali z Wikipedii.

masa = float(input("Podaj swoją masę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
bmi = masa / (wzrost ** 2)

if bmi < 18.5:
    opis = "niedowaga"
elif bmi >= 18.5 and bmi <= 25.0 :
    opis = "pożądana masa ciała"
else:
    opis = "otyłość"

print(f"Twoje BMI wynosi: {bmi:.2f}, co wskazuje na {opis}")
print('Twoje bmi wynosi {:.2f}'.format(bmi))
print('Twoje bmi wynosi'+ str(round(bmi, 2)))

# niedowaga	bmi <= 18.49
# pożądana masa ciała	18.5 – 24.99 optimum	minimalne
# nadwaga	bmi > = 25.0

###################################

x = int(input('podaj wiek'))


#0---------18-----------------------------64------------

if x <18  or x > 64:
    print('osoba w wieku nie-pracującym')
elif x >= 18: and x <= 64
    print('osoba w wieku pracującym')

#-----0---------18-----------------------------64------------

if x < 18 and x>0:
    print('osoba niepelnoletnia')
elif x >= 18:
    print('osoba pelnoletnia')
else:
    print('bledny input - podaj liczbe wieksza od zera')

#-----0---------18-----------------------------64------------

x = float(input('podaj wiek'))
if x <18  or x > 64:
    print('osoba w wieku nie-pracującym')
###### nastepny warunek
if x <= 18:
    print('osoba niepelnoletnia')
#-----0---------18-----------------------------64------------

x = float(input('podaj wiek'))
if x <18  or x > 64:
    print('osoba w wieku nie-pracującym')
###### nastepny warunek
elif x <= 18:
    print('osoba niepelnoletnia')

#-----0---------18-----------------------------64------------

# jak nie robic - nie porownywac roznych typowe danych
x = input('podaj wiek')
if x <18  or x > 64:
    print('osoba w wieku nie-pracującym')
###### nastepny warunek
elif x <= 18:
    print('osoba niepelnoletnia')

#-----0---------18-----------------------------64------------

x = input('podaj wiek')
if x <'18'  or x > '64':
    print('osoba w wieku nie-pracującym')
###### nastepny warunek
elif x <= '18':
    print('osoba niepelnoletnia')


x = input('podaj plec')
if x == 'kobieta':
    print('kobieta')
else:
    print('cos innego')


x = input('podaj litera')
if x > 'c':
    print('wiekszy')
else:
    print('mniejszy')

#-------------------------------------------------------------
x = True
x = False
x = None

if x == True:
    print('True')
else:
    print('False')

##################################
def f(x):
    if x>18:
        return x

x28 = f(15)

if x28 == None:
    print('None')

if x28:
    print('Exists')

if not x28:
    print('Not exists')









