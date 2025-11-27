nev = input("Felhasználónév: ")
jelszo = input("Jelszó: ")

if nev == "admin" and jelszo == "1234":
    print("Sikeres bejelentkezés.")
elif nev != "admin" and jelszo == "1234":
    print("Ismeretlen felhasználó.")
elif nev == "admin" and jelszo != "1234":
    print("Hibás jelszó.")
else:
    print("Helytelen adatok.")