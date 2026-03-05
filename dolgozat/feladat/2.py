# Két szám bekérése
a = float(input("Add meg az első számot: "))
b = float(input("Add meg a második számot: "))

# Relációs jel meghatározása és kiírása
if a < b:
    print(f"{a} < {b}")
elif a > b:
    print(f"{a} > {b}")
else:
    print(f"{a} = {b}")