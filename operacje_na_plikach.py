


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


