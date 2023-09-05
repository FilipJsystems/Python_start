


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

