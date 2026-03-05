import locale

locale.setlocale(locale.LC_ALL, 'hu_HU.UTF-8')

Llista=["Attila", "Anita", "Vilmos", "Áron", "Tamara"]
Llista.sort(key=locale.strxfrm)
print(Llista)