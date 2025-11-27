osszeg = float(input("Add meg a vásárlás összegét: "))

if osszeg < 10000:
    kedv = 0
elif osszeg <= 20000:
    kedv = 0.05
else:
    kedv = 0.10

fizetendo = osszeg * (1 - kedv)

print("Kedvezmény:", kedv * 100, "%")
print("Fizetendő összeg:", fizetendo, "Ft")