import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

osszeg = d1 + d2

print("Dobások:", d1, "és", d2, "- összeg:", osszeg)

if osszeg > 9:
    print("Nagy dobás!")
elif 6 <= osszeg <= 9:
    print("Közepes dobás.")
else:
    print("Kicsi dobás.")