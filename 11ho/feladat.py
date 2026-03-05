word = input("Írj be egy szót: ").strip()
if not word:
    print("Nem adtál meg szót.")
else:
    print(word[::-1]) 

