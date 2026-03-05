Ljegyek = [2, 2, 4, 5, 5, 3]

osszeg = sum(Ljegyek)
darab = len(Ljegyek)
atlag = osszeg / darab
print("A jegyek:", Ljegyek)
print("Az átlag:", "{:.1f}".format(atlag))

# Ha .5 az átlag, kérdezzük meg a javítást
if atlag == int(atlag) + 0.5:
    valasz = input("Az átlag x.5. Szeretnél javítani a jobb jegyért? (i/n): ")
    if valasz.lower() == "i":
        uj = int(input("Add meg a javítás jegyét (2-5): "))
        legrosszabb = min(Ljegyek)
        if uj > legrosszabb:
            idx = Ljegyek.index(legrosszabb)
            Ljegyek[idx] = uj
            print("Kicseréltük a legrosszabb jegyet, új jegyek:", Ljegyek)
        else:
            print("A javítás nem lett jobb, maradnak a jegyek:", Ljegyek)
    else:
        print("Nem javítottál, maradnak a jegyek:", Ljegyek)

# Új átlag és félévi jegy
uj_atlag = sum(Ljegyek) / len(Ljegyek)
if uj_atlag - int(uj_atlag) >= 0.5:
    felev = int(uj_atlag) + 1
else:
    felev = int(uj_atlag)

print("Az új átlag:", "{:.2f}".format(uj_atlag))
print("A félévi jegy:", felev)