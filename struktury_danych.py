############# krotki - po angielsku tuple

# lista - mutable
# krotka - immutable - niemutowalna, niezmienna

# lista moze sie zmieniac pod wzgledem rozmiaru, elementów, ma sporo funkcji na których można działać
# krotka nie może się zmieniać (może zostać jedynie nadpisana). Prawie nie ma żadnych istotnych funkcji

t = tuple([1, 2, 3, 4])
t = (1, 1, 1, 2, 3, 4)

t.count(1)  # liczy ilosc elementow
t.index(4)  # to podaje indeks danego elementu
t.index(1)

for el in t:
    print(el)

length = len(t)

t = tuple(i for i in range(0,100))

# Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
# Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli
