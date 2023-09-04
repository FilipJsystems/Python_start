

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
# Wydrukuj co 2 liczbę z zakresu 1-50   # 

