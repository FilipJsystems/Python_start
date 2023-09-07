# typowy przykład obsługi błędów (najprostszy)

try:
    print('i'+ 9)
except:
    pass


try:
    print('i'+ 2)
except Exception as e:  # złapanie komunikatu, który mowi jaki błąd został popełniony
    print(e)



try:
    print(1/0)
except ZeroDivisionError:                       # specyficzny rodzaj błędu - poniższy print wyświetli się tylko wtedy gdy błąd jest natury ZeroDivisionError
    print("nie można dzielić przez zero!")
except:                                         # jeśli nie, to mamy tutaj generalny except
    print("jakiś inny błąd")

# rodzaje błędów: ZeroDivisionError,IOError, ValueError, TypeError.. i wiele innych..

try:
    print("działa")
except ValueError:
    print("wyjątek")
else:                           # else sprowadza się do alternatywnej sytuacji w momencie gdy powyższy except nie był wykonany
    print("nie bylo wyjatku")


try:
    print("działa")
except:                          # ta sama konstrukcja działa dla niezdefiniowanego exception - wcześniej mi się konsola zacięła i myślałem, że to błąd składni!!!
    print("wyjątek")
else:
    print("nie bylo wyjatku")


try:
    raise TypeError()
except TypeError:
    print("nie ma po co podnosić TypeError")


try:
    print(1/0)
except:
    print("wyjątek")
finally:
    print("co by się nie działo to ja się uruchamiam")  # to się zawsze uruchomi (przy prawidłowej instrukcji w bloku except - jeżeli tam będzie błąd, to program i tak się wysypie)

####################################

# Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
# zeby nie wyskoczyl na błąd - żeby błą nie przerwał dalszej operacji

for i in range(-10, 11):
    try:
        print(1/i)
    except:
        print('error')

###

for i in range(-10, 11):
    try:
        print(1/i)
    except ZeroDivisionError:
        print('dzielenie przez zero')
    except:
        print('jakiś inny błąd')


# Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
# jeżeli jest jakiś błąd - złap go i zapisz w pliku log.txt

import os
path = r'C:\Users\localadmin\PycharmProjects\pythonProject'
filename = 'log.txt'
filename = os.path.join(path, filename)

for i in range(-10, 11):
    try:
        print(1/i)
    except Exception as e:
        print('error', e)
        with open(filename, 'a') as f:
            f.write(str(e)+'\n')        # ważne żebby zamienić 'e' na string


############################################