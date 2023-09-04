

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









