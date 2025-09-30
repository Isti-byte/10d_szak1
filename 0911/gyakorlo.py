import math

ar = float(input("Add meg a termék eredeti árát (Ft): "))
szazalek = float(input("Hány százalékkal csökkent az ár?: "))

uj_ar = ar - (ar * szazalek / 100)

print("Az új ár:", uj_ar, "Ft")