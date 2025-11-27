print("Szerződés készítő")
cim = input("Szerződés címe: ")
fel = input("Felek neve (pl. 'Kovács János'): ")
masik = input("Másik fél neve: ")
targy = input("A szerződés tárgya (röviden): ")
osszeg = input("Ellenszolgáltatás (ha van, pl. '10000 Ft' vagy 'nincs'): ")
datum = input("Dátum (pl. 2025-11-06): ")

szerzodes = ""
szerzodes += cim + "\n\n"
szerzodes += "Szerződő felek:\n"
szerzodes += "1) " + fel + "\n"
szerzodes += "2) " + masik + "\n\n"
szerzodes += "A megállapodás tárgya:\n"
szerzodes += targy + "\n\n"
szerzodes += "Ellenszolgáltatás:\n"
szerzodes += osszeg + "\n\n"
szerzodes += "Egyéb feltételek:\n"
szerzodes += "- A felek a szerződést jóhiszeműen teljesítik.\n"
szerzodes += "- A vita esetén a felek megpróbálnak egyezségre jutni.\n\n"
szerzodes += "Kelt: " + datum + "\n\n"
szerzodes += "Aláírások:\n\n"
szerzodes += fel + " _______________________\n\n"
szerzodes += masik + " _______________________\n"

print("\n--- Szerződés ---\n")
print(szerzodes)

with open("szerzodes.txt", "w", encoding="utf-8") as f:
    f.write(szerzodes)

print("A szerződés elmentve: szerzodes.txt")