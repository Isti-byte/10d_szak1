# Jelszó ellenőrzés stringekkel

def jelszó_ellenőrzés(jelszó):
    """
    Ellenőrzi a jelszó erősségét az alábbi kritériumok alapján:
    - Legalább 8 karakter hosszú
    - Tartalmaz nagybetűt
    - Tartalmaz kisbetűt
    - Tartalmaz számot
    - Tartalmaz speciális karaktert
    """
    
    hibák = []
    
    # Hossz ellenőrzése
    if len(jelszó) < 8:
        hibák.append("❌ A jelszó legalább 8 karakter hosszú kell, hogy legyen")
    
    # Nagybetű ellenőrzése
    ha_nagybetű = False
    for kar in jelszó:
        if kar.isupper():
            ha_nagybetű = True
            break
    if not ha_nagybetű:
        hibák.append("❌ A jelszóban kell nagybetű")
    
    # Kisbetű ellenőrzése
    ha_kisbetű = False
    for kar in jelszó:
        if kar.islower():
            ha_kisbetű = True
            break
    if not ha_kisbetű:
        hibák.append("❌ A jelszóban kell kisbetű")
    
    # Szám ellenőrzése
    ha_szám = False
    for kar in jelszó:
        if kar.isdigit():
            ha_szám = True
            break
    if not ha_szám:
        hibák.append("❌ A jelszóban kell legalább egy szám")
    
    # Speciális karakterek ellenőrzése
    speciális = "!@#$%^&*()_+-=[]{}|;:',.<>?/~"
    ha_speciális = False
    for kar in jelszó:
        if kar in speciális:
            ha_speciális = True
            break
    if not ha_speciális:
        hibák.append("❌ A jelszóban kell speciális karakter: " + speciális)
    
    return hibák


# Interaktív jelszó ellenőrzés
print("=== Jelszó Ellenőrzés ===\n")

while True:
    jelszó = input("Kérlek, írj be egy jelszót (vagy 'kilépés' a kilépéshez): ")
    
    if jelszó.lower() == "kilépés":
        print("Viszlát!")
        break
    
    print(f"\nJelszó: '{jelszó}'")
    hibák = jelszó_ellenőrzés(jelszó)
    
    if not hibák:
        print("✅ A jelszó erős!\n")
    else:
        for hiba in hibák:
            print(hiba)
        print()
