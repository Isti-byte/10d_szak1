import random

hónapok = ["Január","Február","Március","Április","Május","Június",
           "Július","Augusztus","Szeptember","Október","November","December"]

# Generálás - egészre kerekítve -20 és +40 között
hőmérsékletek = []
for _ in range(12):
    hőmérsékletek.append(random.randint(-20, 40))

print("Havi átlaghőmérsékletek:", hőmérsékletek)

# Fagyos hónapok (0 alatt)
fagyos_db = 0
for t in hőmérsékletek:
    if t < 0:
        fagyos_db = fagyos_db + 1
print("Fagyos hónapok száma:", fagyos_db)

# Átlaghőmérséklet
átlag = sum(hőmérsékletek) / len(hőmérsékletek)
print("Átlaghőmérséklet: {:.1f} °C".format(átlag))

# Legmelegebb és leghidegebb hónap
max_h = max(hőmérsékletek)
min_h = min(hőmérsékletek)
max_idx = hőmérsékletek.index(max_h)
min_idx = hőmérsékletek.index(min_h)
print("Legmelegebb hónap:", hónapok[max_idx], "-", max_h, "°C")
print("Leghidegebb hónap:", hónapok[min_idx], "-", min_h, "°C")

# Hőség (>30 °C) esetén üzenet
for i, t in enumerate(hőmérsékletek):
    if t > 30:
        print("Hőség volt ebben a hónapban!", hónapok[i], "-", t, "°C")
import random

hónapok = ["Január","Február","Március","Április","Május","Június",
           "Július","Augusztus","Szeptember","Október","November","December"]

# Generálás - egészre kerekítve -20 és +40 között
hőmérsékletek = []
for _ in range(12):
    hőmérsékletek.append(random.randint(-20, 40))

print("Havi átlaghőmérsékletek:", hőmérsékletek)

# Fagyos hónapok (0 alatt)
fagyos_db = 0
for t in hőmérsékletek:
    if t < 0:
        fagyos_db = fagyos_db + 1
print("Fagyos hónapok száma:", fagyos_db)

# Átlaghőmérséklet
átlag = sum(hőmérsékletek) / len(hőmérsékletek)
print("Átlaghőmérséklet: {:.1f} °C".format(átlag))

# Legmelegebb és leghidegebb hónap
max_h = max(hőmérsékletek)
min_h = min(hőmérsékletek)
max_idx = hőmérsékletek.index(max_h)
min_idx = hőmérsékletek.index(min_h)
print("Legmelegebb hónap:", hónapok[max_idx], "-", max_h, "°C")
print("Leghidegebb hónap:", hónapok[min_idx], "-", min_h, "°C")

# Hőség (>30 °C) esetén üzenet
for i, t in enumerate(hőmérsékletek):
    if t > 30:
        print("Hőség volt ebben a hónapban!", hónapok[i], "-", t, "°C")