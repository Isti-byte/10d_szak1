Lkoltesek = ["1200", "1500", "0", "900", "1400", "3150", "0"]

# Számokká alakítás
koltesek = []
for x in Lkoltesek:
    koltesek.append(int(x))

# Napi átlag
osszeg = sum(koltesek)
napok = len(koltesek)
atlag = osszeg / napok
print("Napi átlagos költés: {:.2f} Ft".format(atlag))

# Hány alkalommal volt 2000 Ft felett
db_nagy = 0
for k in koltesek:
    if k > 2000:
        db_nagy = db_nagy + 1
print("2000 Ft felett volt:", db_nagy, "alkalommal")

# Melyik napon költötte a legtöbbet
nap_nevek = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
max_k = max(koltesek)
nap_index = koltesek.index(max_k)
print("A legtöbbet költötte:", nap_nevek[nap_index], "-", max_k, "Ft")

# Zsebpénz a hét elején és maradvány
zsebpenz = int(input("Mennyi zsebpénzt adtak a hét elején (Ft)? "))
maradek = zsebpenz - osszeg
if maradek > 0:
    print("Maradt pénz a következő hétre:", maradek, "Ft")
elif maradek == 0:
    print("Nem maradt pénz a következő hétre.")
else:
    print("Nem maradt; még hiányzik:", abs(maradek), "Ft")