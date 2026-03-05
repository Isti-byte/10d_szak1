import math

# Két pont koordinátáinak bekérése
x1 = float(input("Add meg az első pont x koordinátáját: "))
y1 = float(input("Add meg az első pont y koordinátáját: "))
x2 = float(input("Add meg a második pont x koordinátáját: "))
y2 = float(input("Add meg a második pont y koordinátáját: "))

# Távolság számítása
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A két pont közötti távolság: {distance}")