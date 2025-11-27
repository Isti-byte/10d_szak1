alak = input("Mit szeretnél kiszámítani? (kör / négyzet): ")

if alak == "kör":
    r = float(input("Add meg a sugár hosszát: "))
    terulet = 3.14159 * r * r
    print("A kör területe:", terulet)

elif alak == "négyzet":
    a = float(input("Add meg az oldal hosszát: "))
    terulet = a * a
    print("A négyzet területe:", terulet)

else:
    print("Ismeretlen alakzat.")