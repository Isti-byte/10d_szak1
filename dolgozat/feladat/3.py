import random

# Feldobás (fej vagy írás)
coin = random.choice(["fej", "írás"])

# Tipp bekérése
guess = input("Tippelj! fej vagy írás? ").strip().lower()

# Eredmény ellenőrzése
if guess == coin:
    print("Gratulálok, eltaláltad!")
else:
    print(f"Sajnos nem talált, a helyes válasz: {coin}")