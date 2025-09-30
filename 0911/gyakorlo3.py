penz = int(input("Mennyi pénzed van? "))

otven = penz // 50
penz = penz % 50

husz = penz // 20
penz = penz % 20

tiz = penz // 10
penz = penz % 10

ot = penz // 5
penz = penz % 5

print("50 Ft-os érme:", otven, "db")
print("20 Ft-os érme:", husz, "db")
print("10 Ft-os érme:", tiz, "db")
print("5 Ft-os érme:", ot, "db")
